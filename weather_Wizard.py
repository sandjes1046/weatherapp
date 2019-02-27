import json
import requests

response = requests.get("https://api.weather.gov/gridpoints/BRO/74,8/forecast/hourly")
data = json.loads(response.text)
wizard=(data['properties']['periods'][0]['shortForecast'])
constant='Sunny'
yes='Looks like a good night to observe!'
message= '{"text": "'+yes+'"}'
print(wizard)
if constant == wizard:
    requests.post(data=message, url="https://hooks.slack.com/services/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")
elif constant != wizard:
    print('It is not a good night to observe')
