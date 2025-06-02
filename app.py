from flask import Flask, request, render_template
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                retail_sales=float(request.form.get('retail_sales')),
                retail_transfers=float(request.form.get('retail_transfers')),
                item_type=request.form.get('item_type')
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")

            return render_template('home.html', results=round(results[0], 2))
        except Exception as e:
            return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
