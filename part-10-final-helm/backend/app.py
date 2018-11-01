import json
import logging
import os
import random

import redis
import requests
from flask import Flask, jsonify

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
app = Flask(__name__)
URL_FOR_QUOTE_DB_WRAPPER = os.environ.get("DAL_URL", "http://localhost:5000")


# We get the number of quotes the DB have
NUMBER_OF_QUOTES = int(requests.get(URL_FOR_QUOTE_DB_WRAPPER + "/quote_len").text)
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
print("Connecting to redis")
r = redis.Redis(host=REDIS_HOST)


def get_quote_with_cache(random_number):
    url_for_quote_request = "/quote/{}".format(random_number)
    url_to_query = URL_FOR_QUOTE_DB_WRAPPER + url_for_quote_request
    # We check if the redis have the quote
    if r.get(random_number):
        logging.info("key: {} found in redis".format(random_number))
        resp = r.get(random_number)
    else:
        # If not we do a request and set the cache
        logging.info("key: {} not found in redis".format(random_number))
        resp = requests.get(url_to_query).text
        r.set(random_number, resp)
    return json.loads(resp)


@app.route("/")
def get_quote():
    """
    :return: return a random quote
    """
    random_number = random.randint(0, NUMBER_OF_QUOTES - 1)
    return jsonify(get_quote_with_cache(random_number))


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
