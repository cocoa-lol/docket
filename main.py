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
if len(arg) >= 2:
    try:
        port = arg[(arg.index("--port") + 1)]
    except IndexError as e:
         raise ValueError("An error has occured while trying to get specified port (if any.) Make sure port is passed like: main.py --port 8080. Error: " + str(e))
else:
    print("[WARNING] Running at high-permission ports like 80 or 443 may raise a permission error. Port: " + str(port))
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/readme')
def readme():
    return render_template("docs/readme.html")

if __name__=="__main__":
    print("Running Docket at " + host + ":" + str(port))
    serve(app, host=host, port=port)