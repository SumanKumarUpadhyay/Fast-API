from pydantic import BaseModel, EmailStr,AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model 
    

    
def insert_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name' : 'Suman', 'age' : 70,'email' : 'suman@hdfc.com', 'linkdin' : 'https://www.linkedin.com/in/suman', 'weight' : 65.5, 'married' : False, 'allergies' : ['peanuts'], 'contact_details' : {'phone' : '123-456-7890', 'emergency_contact' : '987-654-3210'}}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)