from flask import Flask,request

# GET method 

app=Flask(__name__)

@app.route("/",methods=['GET'])
def user_get():
    data=[{"id":1 ,"name":'Alice'},
          {"id":2,"name":"bod"}]
    return data

if __name__=="__main__":
    app.run(debug=True)


