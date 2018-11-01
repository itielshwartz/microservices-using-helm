import json
import os
import random

from flask import Flask, jsonify

app = Flask(__name__)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
QUOTES_FILE_PATH = os.path.join(DIR_PATH, "quotes.json")

with open(QUOTES_FILE_PATH) as f:
    # Quote list
    quotes = json.load(f)


@app.route("/")
def get_quote():
    """
    :return: return a random quote
    """
    random_number = random.randint(0, len(quotes) - 1)
    return jsonify(quotes[random_number])


if __name__ == "__main__":
    app.run("0.0.0.0")
