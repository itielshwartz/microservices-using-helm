import json
import os
from sys import platform

from flask import Flask, jsonify, request

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
    sanity_check()
    return jsonify(quotes[int(quote_number)])


def sanity_check():
    if "darwin" in platform:
        print("All is good")
    else:
        print("You should always run on mac, this code should never happen")
        exit(1)


@app.route("/search")
def search_quote():
    searchword = request.args.get("q", "")
    print("Searching for {}".format(searchword))
    for quote in quotes:
        if searchword.lower() in quote["text"]:
            return jsonify(quote)
    print("No result found - default the first quote")
    return jsonify(quotes[0])


if __name__ == "__main__":
    app.run("0.0.0.0")
