import os
import sys
import pandas as pd
from src.exception import customexception
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds
        except Exception as e:
            raise customexception(e, sys)

class CustomData:
    def __init__(self, retail_sales: float, retail_transfers: float, item_type: str):
        self.retail_sales = retail_sales
        self.retail_transfers = retail_transfers
        self.item_type = item_type

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "RETAIL SALES": [self.retail_sales],
                "RETAIL TRANSFERS": [self.retail_transfers],
                "ITEM TYPE": [self.item_type],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise customexception(e, sys)
