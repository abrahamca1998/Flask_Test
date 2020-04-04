from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import json

app = Flask(__name__)

def get_num_points(num_batch):
    return (num_batch+1)*2

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        percentage_aux = request.form["percentage"]
        capacity_aux=request.form["capacity"]
        min_infected_aux=request.form["min_infected"]
        return redirect(url_for("user", usr=user,percentage=percentage_aux,capacity=capacity_aux,min_infected=min_infected_aux))
    else:
        return render_template("login.html")

@app.route("/<usr>/<capacity>/<min_infected>/<percentage>")
def user(usr,min_infected,percentage,capacity):
   
    dictionary={}
    num_batch=80
    num_points=3
    for i in range(num_batch):
        dictionary["Num_Batch_"+str(i)]={}
        num_points=get_num_points(i)
        for j in range(num_points):
            dictionary["Num_Batch_"+str(i)]["Num_Point_"+str(j)]={}
            dictionary["Num_Batch_"+str(i)]["Num_Point_"+str(j)]={}
    for i in range(num_batch):
        num_points=get_num_points(i)
        for j in range(num_points):
            point=np.random.rand(2,1)
            dictionary["Num_Batch_"+str(i)]["Num_Point_"+str(j)]={'x1':point[0][0],'x2':point[1][0]}
    json_data=json.dumps(dictionary)
    return json_data

if __name__ == "__main__":
    app.run(debug=True)