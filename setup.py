from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

print(f'Secret Key: {secret_key}')
print(f'Debug Mode: {debug}')
