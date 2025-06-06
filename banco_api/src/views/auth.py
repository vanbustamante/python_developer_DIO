from src.schemas.auth import Token 


def format_token_response(access_token: str, token_type: str = "bearer") -> Token:
    return Token(access_token=access_token, token_type=token_type)