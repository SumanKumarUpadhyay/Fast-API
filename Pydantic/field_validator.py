from pydantic import BaseModel, EmailStr,AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError('Not a valid email domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    

    
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

patient_info = {'name' : 'Suman', 'age' : 21,'email' : 'suman@hdfc.com', 'linkdin' : 'https://www.linkedin.com/in/suman', 'weight' : 65.5, 'married' : False, 'allergies' : ['peanuts'], 'contact_details' : {'phone' : '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)