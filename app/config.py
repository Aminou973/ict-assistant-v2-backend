import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis un fichier .env

DATABASE_URL = os.getenv("DATABASE_URL")
