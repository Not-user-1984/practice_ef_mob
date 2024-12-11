from pydantic import BaseModel,  field_validator


class UserCreate(BaseModel):
    name: str
    email: str

    @field_validator("name")
    def validate_name(cls, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return value

    @field_validator("email")
    def validate_email(cls, value, values, **kwargs):
        if "@" not in value:
            raise ValueError("Invalid email format")


class UserResponse(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
