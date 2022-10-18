import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

""" 
- HTTP Request -> HTML Page
- REST Api HTTP Request -> json data (or xml or other)
"""

get_response = requests.get(endpoint)  # HTTP Request
# print(get_response.text)
# print(get_response.json())
# print(get_response.status_code)
