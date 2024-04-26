from mongoengine import Document, FloatField

class PredictionData(Document):
    AREA = FloatField(required=True)
    SHAPEFACTOR_2 = FloatField(required=True)
    MeanRR = FloatField(required=True)
    EntropyRR = FloatField(required=True)