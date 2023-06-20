import sys
import pandas as pd
from flight.exception import CustomException
from flight.utils import load_object
import os


class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","proprocessor.pkl")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Airline: str,
        Source: str,
        Destination: str,
        Total_Stops: str,
        Journey_day: int,
        Journey_month: int,
        Journey_year: int,
        hours: int,
        minutes: int,
        Arrival_hour: int,
        Arrival_min: int,
        duration_hours: int,
        duration_mins: int
        ):

        self.Airline = Airline

        self.Source = Source

        self.Destination = Destination

        self.Total_Stops = Total_Stops

        self. Journey_day =  Journey_day

        self.Journey_month = Journey_month

        self.Journey_year = Journey_year
        self.hours = hours
        self.minutes = minutes
        self.Arrival_hour = Arrival_hour
        self.Arrival_min = Arrival_min
        self.duration_hours = duration_hours
        self.duration_mins= duration_mins

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'Airline':[self.Airline],
                'Source':[self.Source],
                'Destination':[self.Destination],
                'Total_Stops':[self.Total_Stops],
                'Journey_day':[self.Journey_day],
                'Journey_month':[self.Journey_month],
                'Journey_year':[self.Journey_year],
                'hours':[self.hours],
                'minutes':[self.minutes],
                'Arrival_hour':[self.Arrival_hour],
                'Arrival_min':[self.Arrival_min],
                'duration_hours':[self.duration_hours],
                'duration_mins':[self.duration_mins],
                
            }

            df = pd.DataFrame(custom_data_input_dict)

            return df  

        except Exception as e:
            raise CustomException(e, sys)


