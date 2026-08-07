from pydantic import BaseModel, EmailStr, ConfigDict

class Credentials(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: EmailStr 
    password: str

class LoginRequest(Credentials):
    pass

class RegisterRequest(Credentials):
    name: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str

class MessageResponse(BaseModel):
    message: str
