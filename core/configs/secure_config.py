import os
from dotenv import load_dotenv

load_dotenv()

# Secret Key
# You can get one by going to this site https://djecrety.ir/
SECRET_KEY = os.getenv("SECRET_KEY")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")