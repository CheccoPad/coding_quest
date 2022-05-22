import requests

api_request = requests.get('https://codingquest.io/api/puzzledata?puzzle=1')

data = api_request.text

organized_data = data.split()

print(organized_data)

for x in organized_data:
    datum = int(x)

i = 0

while i < 60:

    print(i)
    i += 1

print(f'{datum / 2}')

