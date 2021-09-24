from flask import Flask, Response
import database_services.RDBService as d_service
from flask_cors import CORS
import json

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.imdb_user_resource import IMDBUserResource

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    db_service = d_service.RDBService()
    res = db_service.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/imdb/users/<prefix>')
def get_users_by_prefix(prefix):
    res = IMDBUserResource.get_by_username_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0")
