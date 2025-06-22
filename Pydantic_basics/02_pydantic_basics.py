from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : str = Field(max_length=50)
    email : EmailStr
    linkedn_url : AnyUrl
    age : int
    weight : float = Field(gt=0, lt=120)
    married : bool = False
    allergies : Optional[List[str]] = Field(max_length=5)
    contact_details : Dict[str, str]


patient_info_1 = {'name' : "Sushant", 'email' : 'abc@gmail.com', 'linkedn_url': 'http:/linkedin/2132','age' : 30, 'weight': 72.5, 'married': True, 'allergies': ['pollen', 'shellfish'], 'contact_details' : {'phone': '13563'}}

patient_info_2 = {'name' : "Sushant", 'age' : '30'}

patient1 = Patient(**patient_info_1)
# patient2 = Patient(**patient_info_2)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    
    print('patient inserted')

insert_patient_data(patient1)