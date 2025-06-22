from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the patient in less than 50 Chars', examples=['AKshay', 'justin']) ]
    email : EmailStr
    linkedn_url : AnyUrl
    age : int
    weight : Annotated[float ,  Field(gt=0, lt=120, strict=True)]
    married : Annotated[bool, Field(default=None, title='Marrital Status')]
    allergies : Annotated[Optional[List[str]],  Field(default=None, max_length=5)]
    contact_details : Dict[str, str]
