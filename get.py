import requests

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))

print(response)

print(response.status_code)

print(response.text)

print(response.url)

print(response.headers['Content-Type'])

print(response.json())

print(type(response.json()))
