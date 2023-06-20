import os
import sys
from flight.exception import CustomException
from flight.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Initialize Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

# Create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        logging.info('Data ingestion method Started')
        try:

            cwd = os.getcwd()

            df = pd.read_excel(f'{cwd}/notebooks/data/Data_Train.xlsx')
            
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            logging.info('Train Test Split Initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e, sys)

# Run Data ingestion
#if __name__ == '__main__':
#    obj = DataIngestion()
#    raw_data_ingestion = obj.initiate_data_ingestion()

#    obj2 = DataCleaning()
#    raw_arr = obj2.initiate_data_cleaning()

#    obj3 = DataTransformation()
#    train_arr,test_arr,obj_file_path = obj3.inititate_data_transformation()

#    obj4 = ModelTrainer()
#    print(obj4.initiate_model_trainer(train_arr, test_arr))
