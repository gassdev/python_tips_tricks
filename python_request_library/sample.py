import requests

# payload = {'username': 'testing', 'password': 'testing'}

# r = requests.post('https://httpbin.org/post', data=payload)

# r_dict = r.json()

# print(r_dict.get('form'))



r = requests.get('https://httpbin.org/basic-auth/test/test', timeout=3)
print(r.text)
