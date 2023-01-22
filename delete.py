import requests

username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

payload = {'username': username, 'password': password}
url = 'https://httpbin.org/delete'

response = requests.delete(url, data = payload)

print(response.status_code)

print(response.ok)

print(type(response.text))

print(response.url)

print(response.headers['Content-Type'])

print(response.encoding)