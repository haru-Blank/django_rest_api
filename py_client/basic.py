import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"
endpoint = "http://localhost:8000/api"

""" 
- HTTP Request -> HTML Page
- REST Api HTTP Request -> json data (or xml or other)
"""

# get_response = requests.get(endpoint)  # HTTP Request
# # print(get_response.text)
# print(get_response.json())
# print(get_response.status_code)


get_response = requests.get(
    endpoint, 
    params={"name": "Djan Djan Djangooo"},
    json={"query": "Helo World"}
)
print(get_response.json())
