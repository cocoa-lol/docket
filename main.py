from flask import Flask, render_template, jsonify
from waitress import serve
import sys
from pathlib import Path
import os
from flask_cors import CORS

#Init
arg = sys.argv
port = 80 #Set the default port
host = "0.0.0.0" #0.0.0.0 for all devices to access it
app = Flask(__name__)

CORS(app)
#Parse port argument
if len(arg) >= 2:
    if "--port" in arg:
        if type(arg[arg.index("--port") + 1]) == int:
            port = arg[arg.index("--port") + 1]
            if port in [80, 443]:
                print("[WARNING] Running at high-permission ports like 80 or 443 may raise a permission error. Port: " + str(port)) 

@app.route("/api/sites")
def get_sites():
    sites = []
    for f in Path("templates/docs/").iterdir():
        if f.is_file():
            sites.append(f.name.removesuffix(".html"))
    return jsonify(sites)

@app.route("/")
def index():
    return render_template("index.html")

#Automatically render document pages
@app.route("/docs/<site_name>")
def docs(site_name):
    print("Got request for doc: " + site_name)
    if site_name + ".html" in os.listdir("templates/docs/"):
        print("Served doc: " + site_name)
        return render_template("docs/" + site_name + ".html")
    else:
        print("Failed to serve doc: " + site_name)
        return "Page not found", 404


if __name__ == "__main__":
    serve(app, host=host, port=port)