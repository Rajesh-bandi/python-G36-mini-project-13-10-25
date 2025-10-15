from fastapi import Header, HTTPException, status, Depends


API_TOKEN = "work123"


def get_token_header(x_token: str = Header(...)):
    """Simple header-based token dependency.

    Raises 401 if token is missing or invalid.
    """
    if x_token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid X-Token header")
    return x_token
