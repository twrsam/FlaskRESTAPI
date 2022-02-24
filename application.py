from flask import Flask
from flask_restful import Api,Resource
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from uuid import uuid4 as unique
# app = Flask(--name--)
# api = app(Api)