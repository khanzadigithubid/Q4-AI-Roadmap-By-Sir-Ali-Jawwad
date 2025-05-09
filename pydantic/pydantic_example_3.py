from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="Zain Ahmed",  # Too short
        email="zain.ahmed@example.com",
        addresses=[
            {"street": "321 Pine Rd", "city": "Houston", "zip_code": "77001"},
            {"street": "654 Pine Rd", "city": "Phoenix", "zip_code": "60601"}
                   ],
    )
except ValidationError as e:
    print(e)