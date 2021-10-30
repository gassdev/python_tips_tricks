import requests
import json

r = requests.get('https://imgs.xkcd.com/comics/python.png')

# download image
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# print(r.ok)


# print r.headers in json format
print(json.dumps(dict(r.headers), indent=2))