import json
import os

from flask import Flask, jsonify

app = Flask(__name__)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
QUOTES_FILE_PATH = os.path.join(DIR_PATH, "quotes.json")

with open(QUOTES_FILE_PATH) as f:
    quotes = json.load(f)


@app.route("/quote_len")
def get_quote_len():
    return str(len(quotes))


@app.route("/quote/<quote_number>")
def get_quote(quote_number):
    return jsonify(quotes[int(quote_number)])


if __name__ == "__main__":
    app.run("0.0.0.0")
