from fastapi import HTTPException, status

credential_exception: HTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="It was impossible to authenticate user credential.",
    headers={"www-Authenticate": "Bearer"},
)

