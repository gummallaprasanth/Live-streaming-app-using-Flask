from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route("/")
def Homepage():
    return render_template("index1.html")

@app.route("/sucess/<int:score>")
def sucess(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="fail"
    exp={'score':score,'res':res}
    return render_template("result.html",result=exp)

@app.route("/fail/<int:score>")
def fail(score):
    return "the student is fail"+str(score)

# result checker
@app.route("/results/<int:marks>")
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result="sucess"
    return redirect(url_for(result,score=marks))


# result checker html page
@app.route("/submit",methods=["POST",'GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        math=float(request.form["math"])
        data_science=float(request.form["datascience"])
        total_score=(science+math+data_science)/3
    res=""
    
    return redirect(url_for('sucess',score=total_score))


if __name__=="__main__":
    app.run(debug=True)