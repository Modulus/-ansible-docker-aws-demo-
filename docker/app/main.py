from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello, World! bucket: {os.environ['S3BUCKET']}"