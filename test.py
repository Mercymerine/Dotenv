import os
from dotenv import load_dotenv


#load_dotenv(override =True)
load_dotenv()

API_KEY = os.getenv('API_KEY')
print(API_KEY)
USER = os.getenv('USER')
print(USER)
ADDRESS = os.getenv('ADDRESS')
print(ADDRESS)
ADDRESSES = os.getenv('ADDRESSES')
print(ADDRESSES)

EMAIL = os.getenv('EMAIL')
print(EMAIL)
