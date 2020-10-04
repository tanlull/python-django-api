from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/test', methods=['POST','GET']) 
def bar():
    data = request.args.to_dict()
    print()
    print(type(data))
    data["gender"] = "male"
    data["name"] = "คุณ " + data["name"] 
    print("------------------- Get Parameters---------------------")
    print(data)
    print("---------------------------------------------------------")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')