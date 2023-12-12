from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=["GET"])
def hello():
    print("Hello world")
    return render_template("home.html")

@app.route('/temp',methods=["POST"])
def temp():
    data = request.get_json()
    # print("Html template")
    return data

@app.route('/put',methods=["PUT"])
def putData():
    # print("Html template")
    return "Put method"

@app.route('/delete',methods=["DELETE"])
def DeleteData():
    # print("Html template")
    return "Delete method"
    
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)