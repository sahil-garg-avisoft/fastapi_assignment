from fastapi import FastAPI
from dates_fruits_class_api.models.pydantic_model import InputFeatures
from dates_fruits_class_api.utils.preprocess_data import helper_normalise_and_scale_input_features
from dates_fruits_class_api.models.mongo_model import PredictionData
from dates_fruits_class_api.utils.files_loader import model,pipeline
from mongoengine import connect
from dates_fruits_class_api.config.v1.database_config import mongo_config

app = FastAPI()

@app.post("/predict/")
async def predict(features: InputFeatures):
    user_inputs_array = [
        features.AREA,features.SHAPEFACTOR_2,features.MeanRR,features.EntropyRR
    ]
    
    scaled_inputs = helper_normalise_and_scale_input_features(user_inputs_array,pipeline)
    
    prediction = model.predict(scaled_inputs)
    
    prediction_label=int(prediction[0])
    if prediction_label == 2:
        predictedvalue='DOKOL'
    elif prediction_label == 5:
        predictedvalue='SAFAVI'
    elif prediction_label == 4:
        predictedvalue='ROTANA'
    elif prediction_label == 1:
        predictedvalue='DEGLET'
    elif prediction_label == 6:
        predictedvalue='SOGAY'
    elif prediction_label == 3:
        predictedvalue='SIRAQI'
    elif prediction_label == 0:
        predictedvalue='BERHI'
    
    predicted_data_instance = PredictionData(
    AREA=features.AREA, 
    SHAPEFACTOR_2=features.SHAPEFACTOR_2,
    MeanRR=features.MeanRR,
    EntropyRR=features.EntropyRR)

    predicted_data_instance.save()

    return {"predicted_data": predictedvalue}

@app.get("/health")
async def health():
    return {"status": "ok"}

host="localhost"
port=27017
db_name="date_fruits_class"

# connect(db=db_name, host=f"mongodb://{host}:{port}")

connect(db=db_name, host=f"mongodb://{mongo_config.mongo_host}:{port}")