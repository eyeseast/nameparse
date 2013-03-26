"""
A super-simple app that implements nameparser.HumanName as a JSON webservice.

GET /?name="Bob Smith"
"""

from flask import Flask, request, jsonify
from nameparser import HumanName

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', None)
    if not name:
        return "Give me a name to parse."

    name = HumanName(name)

    return jsonify({
        'title' : name.title,
        'first' : name.first,
        'middle': name.middle,
        'last'  : name.last,
        'suffix': name.suffix
    })


if __name__ == '__main__':
    app.run(debug=True)