# using one model in another model as a field. this is basically a nested model. 

from pydantic import BaseModel


class Address(BaseModel):

    city : str
    state : str
    pin : str


class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address # a very complicated field


address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient_1 = Patient(**patient_dict)

print(patient_1.name)
print(patient_1.age)
print(patient_1.address.pin)
print(patient_1.address.state)


# temp = patient_1.model_dump()

# print(temp)
# print(type(temp))


# OR include exclude fields



# temp = patient_1.model_dump(include = ['name', 'age'])
# temp = patient_1.model_dump(exclude = ['name', 'age'])
temp = patient_1.model_dump(include = {'address' : ['state']})
temp = patient_1.model_dump_json(include = {'address' : ['state']})
print(type(temp))




