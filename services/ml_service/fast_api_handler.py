# services/ml_service/fast_api_handler.py

import pickle
import os
import pandas as pd

class FastApiHandler:
    def __init__(self):
        self.param_types = {
            "item_id": str,
            "model_params": dict
        }

        self.model_path = os.path.join(os.path.dirname(__file__), "../models/model.pkl")
        self.load_model(self.model_path)
        
        self.required_model_params = [
            "floor", "kitchen_area", "living_area", "rooms", "is_apartment", "studio", "total_area", 
            "build_year", "building_type_int", "latitude", "longitude", "ceiling_height", 
            "flats_count", "floors_total", "has_elevator"
        ]

    def load_model(self, model_path: str):
        try:
            with open(model_path, 'rb') as file:
                self.model = pickle.load(file)
            print(f"Model loaded successfully from {model_path}")
        except Exception as e:
            self.model = None
            print(f"Failed to load model: {e}")

    def predict_price(self, model_params: dict) -> float:
        if self.model is None:
            raise ValueError("Model is not loaded")
        
        param_values_list = [model_params[param] for param in self.required_model_params]
        param_values_df = pd.DataFrame([param_values_list], columns=self.required_model_params)
        return self.model.predict(param_values_df)[0]
        
    def check_required_query_params(self, query_params: dict) -> bool:
        if "item_id" not in query_params or "model_params" not in query_params:
            return False
        
        if not isinstance(query_params["item_id"], self.param_types["item_id"]):
            return False
                
        if not isinstance(query_params["model_params"], self.param_types["model_params"]):
            return False
        return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
        if set(model_params.keys()) == set(self.required_model_params):
            return True
        return False
    
    def validate_params(self, params: dict) -> bool:
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
		
    def handle(self, params):
        try:
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params["model_params"]
                item_id = params["item_id"]
                print(f"Predicting for item_id: {item_id} and model_params:\n{model_params}")
                prediction = self.predict_price(model_params)
                response = {
                    "item_id": item_id,
                    "prediction": prediction
                }
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response
