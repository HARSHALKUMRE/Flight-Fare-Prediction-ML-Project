from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from flight.pipeline.prediction_pipeline import CustomData, PredictionPipeline

application = Flask(__name__)
app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            Airline=request.form.get('Airline'),
            Source=request.form.get('Source'),
            Destination=request.form.get('Destination'),
            Total_Stops=request.form.get('Total_Stops'),
            Journey_day=int(request.form.get('Journey_day')),
            Journey_month=int(request.form.get('Journey_month')),
            Journey_year=int(request.form.get('Journey_year')),
            hours=int(request.form.get('hours')),
            minutes=int(request.form.get('minutes')),
            Arrival_hour=int(request.form.get('Arrival_hour')),
            Arrival_min=int(request.form.get('Arrival_min')),
            duration_hours=int(request.form.get('Duration_hours')),
            duration_mins=int(request.form.get('Duration_mins'))
        )

        pred_df = data.get_data_as_data_frame() 

        print(pred_df)
        
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0],2)
        return render_template('index.html', results=results, pred_df=pred_df)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)