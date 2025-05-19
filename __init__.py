from config import SECRET_KEY, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB
from exceptions.controlled_exception import HttpControlledException
from types_dict.http import HttpGlobalResponse
from flask import Flask, jsonify
from flask_cors import CORS
from http import HTTPStatus
from routes import routes

# Settings for App
app = Flask(__name__, static_url_path='')
app.secret_key = SECRET_KEY

# Settings for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Settings for CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["OPTIONS", "POST", "GET", "PUT", "DELETE", "PATCH"],
            "allow_headers": ["Authorization", "Content-Type"],
        }
    },
)

# Catch http global errors
@app.errorhandler(HTTPStatus.NOT_FOUND)
def notFound(e: Exception):
    response: HttpGlobalResponse = {
        "message": HTTPStatus.NOT_FOUND.phrase,
    }
    return jsonify(response), HTTPStatus.NOT_FOUND

@app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
def methodNotAllowed(e: Exception):
    response: HttpGlobalResponse = {
        "message": HTTPStatus.METHOD_NOT_ALLOWED.phrase,
    }
    return jsonify(response), HTTPStatus.METHOD_NOT_ALLOWED

@app.errorhandler(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
def unsupportedMediaType(e: Exception):
    response: HttpGlobalResponse = {
        "message": HTTPStatus.UNSUPPORTED_MEDIA_TYPE.phrase,
    }
    return jsonify(response), HTTPStatus.UNSUPPORTED_MEDIA_TYPE

@app.errorhandler(HTTPStatus.BAD_REQUEST)
def badRequest(e: Exception):
    response: HttpGlobalResponse = {
        "message": HTTPStatus.BAD_REQUEST.phrase,
    }
    return jsonify(response), HTTPStatus.BAD_REQUEST

@app.errorhandler(HttpControlledException)
def controlledException(e: HttpControlledException):
    if app.config["DEBUG"]:
        print(f"Controlled Exception: {e}")
        
    response: HttpGlobalResponse = {
        "message": e.message,
    }
    return jsonify(response), e.code

@app.errorhandler(Exception)
def internalServerError(e: Exception):
    print(f"{HTTPStatus.INTERNAL_SERVER_ERROR.phrase}: {e}")
    
    response: HttpGlobalResponse = {
        "message": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
    }
    return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR

# Routes
for route in routes:
    app.add_url_rule(route["rule_path"], view_func=route["controller"])