
import json

# help(json)


# Serialising

mapping = {
    "Name":"Aju",
    "Age":19,
    "Country":"Nepal"
}
with open("mapping.json", "w") as file:
    json.dump(mapping, file)

# Deserializing

with open("mapping.json", "r") as file:
    info = json.load(file)
print(info)