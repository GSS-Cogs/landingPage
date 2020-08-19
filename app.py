from flask import Flask, jsonify, request
from flask_cors import CORS
from gssutils import Scraper
from markdown import markdown

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    landingPage = request.args.get('landingPage')
    scraper = Scraper(landingPage)
    try:
        return markdown(scraper._repr_markdown_())
    except Exception as err:
        return markdown(str(err))