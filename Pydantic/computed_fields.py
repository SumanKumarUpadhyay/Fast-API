from pydantic import BaseModel, EmailStr,AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)
    
    

    
def insert_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('BMI:', patient.bmi)
    print(patient.contact_details)
    print('inserted')

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name' : 'Suman', 'age' : 30,'email' : 'suman@hdfc.com', 'linkdin' : 'https://www.linkedin.com/in/suman', 'weight' : 65.5, 'height' : 1.75, 'married' : False, 'allergies' : ['peanuts'], 'contact_details' : {'phone' : '123-456-7890', 'emergency_contact' : '987-654-3210'}}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)