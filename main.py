from fastapi import FastAPI, HTTPExce
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import pickle
import pandas as pd

app = FastAPI()
tier_1_cities = [
    "Mumbai", "Delhi", "Bangalore", "Chennai",
    "Kolkata", "Hyderabad", "Pune"
]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi",
    "Visakhapatnam", "Coimbatore", "Bhopal", "Nagpur", "Vadodara",
    "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati",
    "Thiruvananthapuram", "Ludhiana", "Nashik", "Allahabad",
    "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem",
    "Vijayawada", "Tiruchirappalli", "Bhavnagar", "Gwalior",
    "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode",
    "Warangal", "Kolhapur", "Bilaspur", "Jalandhar", "Noida",
    "Guntur", "Asansol", "Siliguri"
]

with open("model.pkl", "rb") as f:
     model = pickle.load(f)

class InputData(BaseModel):
    age : Annotated[int, Field(..., gt= 0, lt=120, description="Age in years")]
    height : Annotated[float, Field(..., gt=0, description="Height in cm")]
    weight : Annotated[float, Field(..., gt=0, description="Weight in kg")]
    income_lpa : Annotated[float, Field(..., ge=0, description="Annual income")]
    smoker : Annotated[bool, Field(..., description="Whether the person is a smoker")]
    city : Annotated[str, Field(..., description="City of residence")]
    occupation: Annotated[Literal["retired","freelancer","student","government_job",
    "business_owner","unemployed","private_job"], Field(..., description="Occupation")]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / ((self.height / 100) ** 2)
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
@app.post("/predict")
def predict(user : InputData):
    input_df = pd.DataFrame([{
        "bmi": user.bmi,
        "age_group": user.age_group,
        "lifestyle_risk": user.lifestyle_risk,
        "city_tier": user.city_tier,
        "income_lpa": user.income_lpa,
        "occupation": user.occupation

    }])

    model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predicted_premium": float(model.predict(input_df)[0])})