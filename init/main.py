import requests


url = " http://numbersapi.com/ "

req = requests.get(url)

if req.status_code == 200:
    print(req.text)
else:
    print(req.status_code)