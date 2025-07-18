from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))



# temp = patient_1.model_dump()

# print(temp)
# print(type(temp))


# OR include exclude fields



# temp = patient_1.model_dump(include = ['name', 'age'])
# temp = patient_1.model_dump(exclude = ['name', 'age'])
temp = patient_1.model_dump(include = {'address' : ['state']})
temp = patient_1.model_dump_json(include = {'address' : ['state']})
print(type(temp))
