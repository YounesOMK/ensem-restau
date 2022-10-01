from typing import Optional

import requests
from restau_servant.config import LOGIN_URL, MY_ACCOUNT_URL

class User:
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def authenticate(self, through: str = LOGIN_URL) -> Optional[requests.Session]:
        
        session = requests.Session()
        login_response = session.post(through, data={
            "username": self.username,
            "password": self.password,
            "login": "",
            "page": "index"
        })
        
        logged_in = session.get(MY_ACCOUNT_URL, allow_redirects=False).status_code == 200
        if not logged_in:
            raise ValueError('Probably incorrect credentials.')
        
        return session
    
        