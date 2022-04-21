import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print ('before update: ', response.json())

todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())