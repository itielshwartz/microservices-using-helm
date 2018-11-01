import os
import random

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
URL_FOR_QUOTE_DB_WRAPPER = os.environ.get("DAL_URL", "http://localhost:5000")


# We get the number of quotes the DB have
NUMBER_OF_QUOTES = int(requests.get(URL_FOR_QUOTE_DB_WRAPPER + "/quote_len").text)


@app.route("/")
def get_quote():
    """
    :return: return a random quote
    """
    random_number = random.randint(0, NUMBER_OF_QUOTES - 1)
    url_for_quote_request = "/quote/{}".format(random_number)
    return jsonify(
        requests.get(URL_FOR_QUOTE_DB_WRAPPER + url_for_quote_request).json()
    )


@app.route("/search")
def search_quote():
    searchword = request.args.get("q", "")
    return jsonify(
        requests.get(
            URL_FOR_QUOTE_DB_WRAPPER + "/search", params={"q": searchword}
        ).json()
    )


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
