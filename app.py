from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)


@app.route("/")

def house():
    return render_template("index1.html")




if __name__=="__main__":
    app.run(debug=True)