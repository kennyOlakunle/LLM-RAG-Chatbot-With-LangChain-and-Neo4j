from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
debug = os.getenv('DEBUG')

print(f'Secret Key: {OPENAI_API_KEY}')
print(f'Debug Mode: {debug}')
