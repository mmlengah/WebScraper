import os
from dotenv import load_dotenv

class CredentialLoader:
    def __init__(self):
        load_dotenv()
    
    def load_credentials(self):
        credentials = {
            'username': os.getenv('BRIGHT_DATA_USERNAME'),
            'password': os.getenv('BRIGHT_DATA_PASSWORD'),
            'host': os.getenv('BRIGHT_DATA_HOST')
        }
        
        if not all(credentials.values()):
            missing = [key for key, value in credentials.items() if not value]
            raise EnvironmentError(f"Missing credentials: {', '.join(missing)} in the .env file.")
        
        return credentials