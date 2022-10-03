from datetime import datetime
import os
from flask import (
    Flask,
    render_template,
    make_response,
    redirect,
    request,
    url_for,
    jsonify,
    Blueprint,
    current_app as app,
)
import markdown

import stripe
from nanoid import generate
from flask_login import login_required
import requests
# import pycountry

main = Blueprint("main", __name__)




# from flask import Flask, request, render_template,url_for
# import markdown
# import requests
# import os
# import stripe
# from dotenv import load_dotenv

# app = Flask(__name__)
# load_dotenv()

stripe.api_key = os.getenv("STRIPE_API_KEY")
@main.get("/")
def index():
    headers = {"Authorization": f"Bearer {os.getenv('TWITTER_BEARER_TOKEN')}"}

    r = requests.get(
        "https://api.twitter.com/2/tweets/search/recent?query=from:liberioltre",
        headers=headers,
    )
    tweets = r.json()["data"][:3]
    return render_template("index.html", tweets=tweets)


@main.route("/post/<path:path>/")
def posts(path):
    f = open(f"./posts/{path}.md", "r")
    htmlmarkdown = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "meta", "footnotes", "toc", "tables"]
    )
    post = htmlmarkdown.convert(f.read())
    return render_template("post.html", post=post, meta=htmlmarkdown.Meta)


@main.get("/statuto")
def statuto():
    return render_template("statuto.html")

@main.get("/associati")
def associati():
    return render_template("associati.html")

@main.get("/redazione")
def redazione():
    return render_template("redazione.html")

@main.route("/pay", methods=["GET", "POST"])
def pay():
    if request.method == "GET":
        # stripe needs this format
        return_url = os.getenv("SITE") + url_for("statuto")
        # orderSlug = request.cookies.get("orderSlug")
        order = {"total":"90"}
        intent = stripe.PaymentIntent.create(
            # qua questo 90 deve essere diversamente pescato
            amount=int(90 * 100),
            currency="eur",
            automatic_payment_methods={"enabled": True},
        )
        return render_template(
            "pay.html",
            order=order,
            client_secret=intent.client_secret,
            return_url=return_url,
        )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
