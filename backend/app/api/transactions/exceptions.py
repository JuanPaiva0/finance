from app.core.handlers import AppException

class TransactionNotFoundException(AppException):
    def __init__(self, message: str = "Transaction not found or access denied"):
        super().__init__(message, status_code=404)

class NoFieldsUpdateException(AppException):
    def __init__(self, message: str = "No fields to update"):
        super().__init__(message, status_code=400)

