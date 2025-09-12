from flask import Flask,jsonify,request,render_template
import json
app = Flask(__name__)

def getallToDos():
    with open("db.json") as f:
        return json.load(f)    #ya with mule python apoap file close krel!!
        # return file.read()
def addToDo(data):
    with open("db.json","w") as  file:
        json.dump(data,file,indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["POST"])
def createToDo():
    body = request.json
    data = getallToDos()
    test ={
        "id":len(data)+1,
        "task":body["task"]
    }
    data.append(test)
    addToDo(data)
    # print(body)
    return "todo create success"

@app.route("/read",methods=["GET"])
def readToDo():
    data = getallToDos()
    return jsonify(data)

@app.route("/update/<int:tid>",methods=["PUT"])
def updateToDo(tid):
    data = request.json
    allToDos = getallToDos()
    ToDos = []
    for item in allToDos:
        if item["id"] == tid:
            item["task"] = data["task"]
        ToDos.append(item)  
    addToDo(ToDos)      
    # print(tid)
    # print(data)
    return"todo update success"

@app.route("/delete/<int:tid>",methods=["DELETE"])
def deleteToDo(tid):
    data = getallToDos()
    todos=[]
    for item in data:
        if item in data:
            if item["id"] != tid:
                todos.append(item)
    addToDo(todos)            
    return "todo delete success"
# http://localhost:5000     te postman chya ithe ha pn url takla tr chalto,


if __name__=="__main__":
    app.run(debug=True)





