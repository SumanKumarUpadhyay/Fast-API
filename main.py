# import FastAPI
from fastapi import FastAPI
import json


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return {"message": "Patients management System Api"}

@app.get('/about')
def about():
    return {"message": "A fully functional API for managing patients, appointments, and medical records in a healthcare setting."}

@app.get('/view_patients')
def view_patients():
    data = load_data()
    return data 