from fastapi import FastAPI, Path, HTTPException , Query
import json

app = FastAPI()

def load_data():
    with open("req.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
def hello_world():
    return {"message" : "Hello"}

@app.get("/view")
def view_data():
    data = load_data()
    return data

@app.get("/details/{id}")
def view_patient(id : str = Path(..., description="The Id of the patient in Db", example="P001" )):
    data = load_data()

    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_para(sort_by: str = Query(..., description="Sort on the basics of height and weight"), order: str = Query('asc', description="sort in asc or desc order")):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid sort_by field. Must be one of {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    
    data = load_data()