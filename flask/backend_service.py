
#!/usr/bin/env python3

import logging
import json

import connexion
from connexion import NoContent
from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId
from flask import jsonify
import json
import flask
import requests
import base64
import os
from io import BytesIO
from urllib.parse import urlparse

from backend_const import REQUEST_TIMEOUT
import subprocess
#from app import app
def service(display_name, upfile):  
	logging.debug ("dans predict genre\n")
	print(type(upfile))
	with open("fileToSave.wav", "wb") as fh:
		fh.write(upfile.read())
	#app_name = os.getenv("APP_NAME")

	if True:
		process = subprocess.Popen(['python', './app/gtzankeras/src/app.py', '-t', 'ml', '-m', './app/gtzankeras/models/pipe_svm.joblib', '-s', 'fileToSave.wav'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		returncode = process.wait()
		return(process.stdout.read().decode("utf-8"))


