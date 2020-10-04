import requests 
URL = "http://localhost/all"

r = requests.get(url = URL) 
data = r.json() 

print(data)
print("------ 1 -------")
print(data[1])
print("----- 2 --------")
print(data[2])
print(data[2]["age"])
print(data[2]["name"])
print("----- Loop --------")
for d in data:
    print(d)
print("----------END LOOOP-------")

