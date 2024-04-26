import pickle

with open('dates_fruits_class_api/data_files/model_random_forest.pkl', 'rb') as f:
    model = pickle.load(f)

with open('dates_fruits_class_api/data_files/pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)