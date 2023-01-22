import requests

username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

payload = {'username': username, 'password': password}
url = 'https://httpbin.org/post'

response = requests.post(url, data = payload)

print(response.status_code)

print(response.ok)

print(response.content)

print(response.text)

print(type(response.text))

print(response.url)

print(response.headers['Content-Type'])

print(response.encoding)