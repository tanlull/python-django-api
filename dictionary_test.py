# dictionary
data = {'age':'25', 'name':'เจน'} 
print(type(data))

#Access Dictionary
print(data["name"])

#Modify Dict
data["name"] = "นุ่น"
print(data["name"])

# add dict
data["friend"] = "โบ"
print(data)

#delete dict
del data["friend"]
print(data)