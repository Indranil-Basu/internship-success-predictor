from fastapi import FastAPI
import joblib
import numpy as np
from typing import Literal
from pydantic import BaseModel
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load('placement_model.pkl')

class StudentData(BaseModel):
    CGPA : float
    Internships : int
    Projects : int
    WorkshopsCertifications: int
    AptitudeTestScore : int
    SoftSkillsRating: float
    ExtracurricularActivities : Literal[ 'Yes','No']
    PlacementTraining : Literal['Yes' , 'No']
    SSC_Marks : int
    HSC_Marks : int
@app.post('/predict')
def predict(student : StudentData):
    ExtracurricularActivities = 1 if student.ExtracurricularActivities == 'Yes' else 0
    PlacementTraining = 1 if student.PlacementTraining == 'Yes' else 0
    input_data = np.array([[
        student.CGPA,
        student.Internships,
        student.Projects,
        student.WorkshopsCertifications,
        student.AptitudeTestScore,
        student.SoftSkillsRating,
        ExtracurricularActivities,
        PlacementTraining,
        student.SSC_Marks,
        student.HSC_Marks
    ]])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    return {"placement_status": "Placed" if prediction[0] == 1 else "Not Placed",
            "confidence": round(float(probability)*100,2)
            }