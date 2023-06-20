import os
import sys
from flight.logger import logging
from flight.exception import CustomException
import pandas as pd

from flight.components.data_ingestion import DataIngestion
from flight.components.data_cleaning import DataCleaning
from flight.components.data_transformation import DataTransformation
from flight.components.model_trainer import ModelTrainer

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            return train_data_path, test_data_path
        except Exception as e:
            raise CustomException(e, sys)

    def start_data_cleaning(self, train_data_path, test_data_path):
        try:
            data_cleaning = DataCleaning()
            train_data_path_cleaned, test_data_path_cleaned = data_cleaning.initiate_data_cleaning(train_data_path, test_data_path)
            return train_data_path_cleaned, test_data_path_cleaned
        except Exception as e:
            raise CustomException(e, sys)

    def start_data_transformation(self, train_data_path_cleaned, test_data_path_cleaned):
        try:
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path_cleaned, test_data_path_cleaned)
            return train_arr, test_arr
        except Exception as e:
            raise CustomException(e, sys)

    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_trainer.initiate_model_trainer(train_arr, test_arr)
        except Exception as e:
            raise CustomException(e, sys)


    def start_training(self):
        try:
            train_data_path, test_data_path = self.start_data_ingestion()
            train_data_path_cleaned, test_data_path_cleaned = self.start_data_cleaning(train_data_path, test_data_path)
            train_arr, test_arr = self.start_data_transformation(train_data_path_cleaned, test_data_path_cleaned)
            self.start_model_training(train_arr, test_arr)
        except Exception as e:
            raise CustomException(e, sys)


if __name__=='__main__':
    training_pipeline = TrainingPipeline()
    training_pipeline.start_training()