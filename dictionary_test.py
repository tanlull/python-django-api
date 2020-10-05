
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

books = ['Harry Potter','One POiece','Doraemon']
tel = {'office':'025051122','home':'022798129','mobile':'0896622733'}

data["book"] = books
data["tel"] = tel
print(data)
