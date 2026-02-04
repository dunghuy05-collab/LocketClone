from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_token
from services.user_service import get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')

def get_current_user(db:Session=Depends(get_db),
                     token: str=Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload or 'sub' not in payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = payload['sub']

    user = get_user_by_id(db,int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user