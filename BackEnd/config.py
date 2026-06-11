from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent / "api_key.env"

resultado = load_dotenv(env_path)

NASA_API_KEY = os.getenv("NASA_API_KEY")
