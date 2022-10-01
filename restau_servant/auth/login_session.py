from typing import Optional
from .user import User


login_session = None

def start_login_session(username: str, password: str):

    global login_session
    if not login_session:
        login_session = User(username, password).authenticate()      
        
    return login_session
