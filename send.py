import requests

headers = dict()

headers['Authrization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyMzQ5NjI3LCJqdGkiOiJiOGRkZDg2MWQ3OGM0ZWFlOGNiMzQyZDZjYTNjMGQwMSIsInVzZXJfaWQiOjF9.qTQH6uVJoQJr1op7iqXtsIfISi3KEKR7IIFI9vx_0q0'

r = requests.get('http://127.0.0.1:8000/paradigms/', headers=headers)

print(r.text)