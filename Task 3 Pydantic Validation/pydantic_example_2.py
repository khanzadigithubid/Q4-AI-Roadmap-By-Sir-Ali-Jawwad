from pydantic import BaseModel, EmailStr

# Define a nested model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class UserWithAddress(BaseModel ): #A base class for creating Pydantic models.
    id: int
    name: str
    email: EmailStr  # Built-in validator for email format
    addresses: list[Address]  # List of nested Address models


# Valid data with nested structure
user_data = {
    "id": 1,
    "name": "Khanzadi",
    "email": "khanzadiwazirali9@gmail.com",
    "addresses": [
        { "street": "123 Main St", "city": "Brooklyn", "state": "NY", "zip_code": "11201"},
        {"street": "456 Oak Ave", "city": "San Diego", "state": "CA", "zip_code": "92101"},
    ],
}
user = UserWithAddress.model_validate(user_data)
print(user.model_dump()) #Return the representation of dictionary