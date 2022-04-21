import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print ('before delete: ', response.json())

response = requests.delete(api_url)
print('after delete: ', response.json())