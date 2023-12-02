import json
import time

a = []
try:
    with open("save.json","r") as file:
        previous_data = json.load(file)
        print(previous_data)
    for item in range(1000000000000000):
        time.sleep(1)
        a.append(item)
except KeyboardInterrupt:
    json_striing = json.dumps(a)
    with open("save.json","a") as file:
        json.dump(json_striing, file)
