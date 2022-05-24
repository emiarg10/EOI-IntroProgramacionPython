import requests
import json

r = requests.get('http://api.open-notify.org/iss-now.json')
print('1:', type(r))
print('2:', r.headers)
print('3:', r.headers['content-type'])
print(f'4: {r.status_code}/{r.encoding}')
print('5:', r.text)
print('6:', r.json()['iss_position'])

u = {'Nombre':'Emi','Apellidos':'Salvachua'}
r = requests.post('http://postman-echo.com/post',data=u)
print(r.text)

url = 'http://httpbin.org/post'
user = json.dumps({'Username' : 'Billy'})
headers = {'content-type' : 'application/json'}
r = requests.post(url,data=user,headers=headers)
print(r.text)