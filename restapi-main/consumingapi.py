import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
result = response.json()
statuscode = response.status_code
headers = response.headers["Content-Type"]
print(result)
print('status code: ', statuscode)
print('headers: ', headers)
