import requests
import json

key ='308a7919a4efeb213f7f6e6a9e08682b'
cities = ['Seoul,KR', 'Tokyo,JP']

api = "https://api.openweathermap.org/data/2.5/weather?q={name}&appid={key}"

for name in cities:
    url = api.format(name = name, key = key)
    res = requests.get(url)

    data = json.loads(res.text)
    print(data)
    print(data['weather'][0]['description'])