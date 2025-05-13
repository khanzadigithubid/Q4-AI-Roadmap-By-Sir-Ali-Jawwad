from pydantic import BaseModel, ValidationError, StrictStr , StrictInt, EmailStr

# define a simple model
class User(BaseModel):
    id: StrictInt
    name: StrictStr
    age: StrictInt | None = None
    email : EmailStr
# Valid data
user_data = {"id": 1, "name": "Khanzadi", "email": "khanzadiwazirali9@gmail.com", "age": 21}
user = User(**user_data)
print(user)  
print(user.model_dump()) 

# Invalid data (will raise an error)
try:
    # invalid_user = User(id="not_an_int", name="Ali", email="ali@example.com")
    user =  User(id = 1, name = 'Khanzadi', email = 'khanzadiwazirali9@gmail.com' )
except ValidationError as e:
    print(e)