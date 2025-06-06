from fastapi import HTTPException, status

class InsufficientFundsException(HTTPException):
    def __init__(self, detail: str = "Saldo insuficiente para realizar a operação."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class InvalidTransactionTypeException(HTTPException):
    def __init__(self, detail: str = "Tipo de transação inválido."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class InvalidAmountException(HTTPException):
    def __init__(self, detail: str = "O valor da transação deve ser positivo."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class AccountAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "Número da conta já registrado."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class AccountNotFoundException(HTTPException):
    def __init__(self, detail: str = "Conta não encontrada."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class CredentialsException(HTTPException):
    def __init__(self, detail: str = "Não foi possível validar as credenciais."):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )
        