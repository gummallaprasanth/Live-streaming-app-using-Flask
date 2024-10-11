from fastapi import FastAPI
import uvicorn


app=FastAPI()

@app.get("/")
def index():
    return "hi i am prasanth"
@app.get("/name")
def Get_name(name : str):

    return "hi i am "+name

@app.get("/score")
def Get_name(name : int):

    return "hi i am "+str(name)



if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)