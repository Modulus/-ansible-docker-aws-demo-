from flask import Flask
from flask import request
import os
import boto3
import sys

import logging


logger = logging.getLogger("docker-demo-app")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



app = Flask(__name__)

logger.info("Application ready to handle requests")

@app.route("/", methods=["GET"])
def hello_world():
    client = boto3.client('s3')
    client.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
    return f"Hello, World! bucket: {os.environ['S3BUCKET']}"

@app.route("/doc", methods=["POST"])
def handle_pdf():
    logger.info("Handling post")
    client = boto3.resource('s3')
    bucket_name = os.environ["S3BUCKET"]
    s3_object=request.args.get("url")
    target="/tmp/f{s3_object}"

    logger.info("Using s3 bucket f{bucket} to download file f{s3_object}")
    logger.info("File will be placed here: f{target}")

    client.Bucket(bucket_name).download_file(s3_object, f"{target}")

    #client.meta.client.download_file(f'{bucket}', f"{s3_object}", '/tmp/f{s3_object}')
    return f"Posted"