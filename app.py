from flask import Flask, render_template
import plotly
import plotly.graph_objects as go 
import chart_studio.plotly as csp
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/plot1", methods=['POST', 'GET']
)
def plot1():
    return render_template("plot1.html")


@app.route("/plot2", methods=['POST','GET'])
def plot2():
    return render_template("plot2.html")

@app.route("/plot3", methods=['POST','GET'])
def plot3():
    return render_template("plot3.html")

if __name__ == "__main__":
    app.run(debug=True)
