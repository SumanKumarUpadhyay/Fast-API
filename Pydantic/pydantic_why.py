from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    
def insert_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name' : 'Suman', 'age' : 21}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)