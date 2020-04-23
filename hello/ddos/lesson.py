import requests

response = requests.get('https://skillbox.ru')
print(response.status_code)
print(response.text)

