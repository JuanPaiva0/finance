from app.core.exceptions import AppException

class NoFieldsUpdateException(AppException):
    def __init__(self, message: str = "No fields to update"):
        super().__init__(message, status_code=400)

class CategoryNotFoundException(AppException):
    def __init__(self, message: str = "Category not found or access denied"):
        super().__init__(message, status_code=404)

class CategoryAlreadyExistsException(AppException):
    def __init__(self, message: str = "You have already a categeory with this name"):
        super().__init__(message, status_code=409)
