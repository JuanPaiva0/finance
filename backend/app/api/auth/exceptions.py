from app.core.exceptions import AppException

class UserAlreadyExistsException(AppException):
    def __init__(self, message: str = "User already exists"):
        super().__init__(message, status_code=409)

class InvalidCredentialsException(AppException):
    def __init__(self, message: str = "Invalid email or password"):
        super().__init__(message, status_code=401)