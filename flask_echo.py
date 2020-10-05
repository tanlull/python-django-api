from flask import Flask, request, jsonify
import json
app = Flask(__name__)

#test
@app.route('/echo', methods=['POST','GET']) 
def foo():    
    data = request.json
    print(type(data))
    books = ['Harry Potter','One POiece','Doraemon']
    tel = {'office':'025051122','home':'022798129','mobile':'0896622733'}

    data["book"] = books
    data["tel"] = tel
    print()
    print("------------------------- ECHO --------------------------")
    print(data)
    print("---------------------------------------------------------")
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


