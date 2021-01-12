import json


with open('test_data.json') as data_file:
    data = json.load(data_file)

print(f"{data[0]} turns on as expected")