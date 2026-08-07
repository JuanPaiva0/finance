import time
from typing import Annotated
from uuid import uuid4
from typing import Literal

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from app.core.config import settings

SECRET = settings.jwt_secret
ALGORITHM = "HS256"

# Payload interno do token decodificado
class TokenPayload(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

# Resposta do endpoint de login
class TokenResponse(BaseModel):
    access_token: str
    token_type: Literal["Bearer"] = "Bearer"

def sign_jwt(user_id: int) -> TokenResponse:
    now = time.time()

    payload = {
        "iss": "financial-control-api",
        "sub": str(user_id),
        "aud": "financial-api",
        "exp": now + (60 * 30),  # 30 minutos
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }

    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return TokenResponse(
        access_token=token
    )

async def decode_jwt(token: str) -> TokenPayload | None:
    try:
        decoded_token = jwt.decode(
            token,
            SECRET,
            audience="financial-api",
            algorithms=[ALGORITHM]
        )

        payload = TokenPayload.model_validate(decoded_token)

        # valida expiração manual (opcional, PyJWT já faz isso)
        if payload.exp < time.time():
            return None

        return payload

    except Exception as e:
        print("JWT Error:", e)
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> TokenPayload:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        # valida presença do token
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token não informado."
            )

        # valida esquema Bearer
        if scheme != "Bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Esquema de autenticação inválido."
            )

        payload = await decode_jwt(credentials)

        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido ou expirado."
            )

        return payload


async def get_current_user(
    token: Annotated[TokenPayload, Depends(JWTBearer())]
) -> dict[str, int]:
    return {"user_id": int(token.sub)}


def login_required(
    current_user: Annotated[dict[str, int], Depends(get_current_user)]
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado."
        )

    return current_user