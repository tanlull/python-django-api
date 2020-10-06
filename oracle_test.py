import oracle_crud as crud

crud.connect()
data_to_insert = (6, 'สมเจตน์', 26,'male')
crud.insert(data_to_insert)
# crud.updateTable(6,10)
# crud.deleteData(10)
crud.selectAll()
crud.close()
