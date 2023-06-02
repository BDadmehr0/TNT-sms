# Dadmehr - Garfox
# packages
import requests
import random
from fake_useragent import UserAgent



for i in range(50):
    ua = UserAgent()
    user = ua.random
    print(user)
