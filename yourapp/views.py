from flask import Blueprint, render_template, request, jsonify

view = Blueprint("view", __name__)


@view.route("/", methods=['GET'])
def hello():
    r = request.headers
    print(r)
    return render_template("index.html"), 200


@view.route("/data", methods=['GET'])
def data():
    return jsonify({"name": "Toto",
                    "age": 30}), 200

# endpoint using query strings
# endpoint using parameters
