from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    email: EmailStr

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str | None = None
    email: EmailStr | None = None

class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)