import os
import sys
from flight.exception import CustomException
from flight.logger import logging
from flight.pipeline.prediction_pipeline import PredictionPipeline
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from dataclasses import dataclass

TIMESTAMP = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

@dataclass
class BatchPredictionConfig:
    inbox_dir = os.path.join("data","inbox")
    outbox_dir = os.path.join("data","outbox")
    archive_dir = os.path.join("data","archive")
    os.makedirs(outbox_dir, exist_ok=True)
    os.makedirs(archive_dir, exist_ok=True)


class BatchPrediction:

    def __init__(self, batch_config:BatchPredictionConfig):
        try:
            self.batch_config = batch_config
        except Exception as e:
            raise CustomException(e, sys)

    def start_prediction(self):
        try:
            input_files = os.listdir(self.batch_config.inbox_dir)

            if len(input_files) == 0:
                logging.info(f"No file found hence closing the batch prediction")
                return None
            
            flight_estimator = PredictionPipeline()
            for file_name in input_files:
                data_file_path = os.path.join(self.batch_config.inbox_dir,file_name)
                df:DataFrame = pd.read_csv(data_file_path)
                prediction_df = flight_estimator.predict(df)
                prediction_file_path = os.path.join(self.batch_config.outbox_dir,f"{file_name}_{TIMESTAMP}")
                pd.DataFrame(prediction_df).to_csv(prediction_file_path)

                archive_file_path = os.path.join(self.batch_config.archive_dir,f"{file_name}_{TIMESTAMP}")
                df.to_csv(archive_file_path)
        except Exception as e:
            raise CustomException(e, sys)