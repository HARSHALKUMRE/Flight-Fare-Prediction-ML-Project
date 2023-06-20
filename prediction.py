from flight.pipeline.batch_prediction import BatchPrediction
from flight.pipeline.batch_prediction import BatchPredictionConfig


if __name__=="__main__":
    config = BatchPredictionConfig()
    flight_batch_prediction = BatchPrediction(batch_config=config)
    flight_batch_prediction.start_prediction()