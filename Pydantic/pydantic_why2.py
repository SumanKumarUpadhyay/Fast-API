from pydantic import BaseModel, EmailStr,AnyUrl, Field
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50,title="Patient Name", description= "Name of the patient, max length 50 characters", example="Suman Kumar")]
    email: EmailStr
    linkdin : AnyUrl
    age: int = Field(gt=0, lt=120, description="Age must be between 1 and 120")
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Optional[bool] = None
    allergies: List[str]
    contact_details: Dict[str, str]
    
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

patient_info = {'name' : 'Suman', 'age' : 21,'email' : 'suman@example.com', 'linkdin' : 'https://www.linkedin.com/in/suman', 'weight' : 65.5, 'married' : False, 'allergies' : ['peanuts'], 'contact_details' : {'phone' : '123-456-7890'}}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)