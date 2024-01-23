from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def check_password(password: str, hash_password: str) -> bool:
    """
    Function to validate if valid password. Compares the 
    password informed by user with hash saved in data base.
    """
    return CRIPTO.verify(password, hash_password)

def hash_password_genarator(password: str) -> str:
    """
    Function to generate hash based on password.
    """
    return CRIPTO.hash(password)