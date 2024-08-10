import json
import cv2 as cv

with open('./config.json', 'r') as f:
    data = json.load(f)

print(data.items())

for prop, value in data.items():
    print('Prop ' + prop + ' value ' + value)
    print(getattr(cv, prop))