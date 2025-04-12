from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {'name': 'sushant', 'age': 32, 'email': 'sushant@gmail.com'}

student = Student(**new_student)
print(student)



# Convert the Pydantic model instance to a dictionary
student_dict = dict(student)

# Access and print the 'age' field from the dictionary
print(student_dict['age'])

# Serialize the Pydantic model instance to a JSON string
student_json = student.model_dump_json()