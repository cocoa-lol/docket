from flask import render_template
from flask import Flask
from flask import url_for
from waitress import serve
import sys
import os
from flask import send_from_directory

#args: --port [int]
host = "0.0.0.0"
port = 80 #Set the default port
arg = sys.argv
app = Flask(__name__)

print("arg: " + str(arg))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/readme')
def readme():
    return render_template("docs/readme.html")

if __name__=="__main__":
    print("Running Docket at " + host + ":" + str(port))
    serve(app, host=host, port=port)