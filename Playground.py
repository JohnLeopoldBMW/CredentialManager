import json


with open("Credentials.json", "r") as f:
    data_old = json.load(f)

with open("new.json", "r") as f:
    data_new = json.load(f)

data = {
    "credentials": data_old["credentials"] + data_new["credentials"]
}

with open("Credentials.json", "w") as f:
    json.dump(data, f, indent=4)


print("Data old:")
print(data_old)
print("Data new:")
print(data_new)
print("\n")
print("Data current:")
print(data)
