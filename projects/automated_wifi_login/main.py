import requests
import dotenv
import os

# getting the url from .env file
dotenv.load_dotenv()
# url_login = "http://hs1-4-amplus.spot/login?dst=&username=xxxxxxxxxxxxxxxxxxxxxxxxxxx"
url_login = os.getenv("url")

# print the url to verify
print(url_login)

# get request
response = requests.get(url_login)