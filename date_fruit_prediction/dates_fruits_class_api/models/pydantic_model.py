from pydantic import BaseModel

class InputFeatures(BaseModel):
    AREA: float
    SHAPEFACTOR_2: float
    MeanRR: float
    EntropyRR: float
