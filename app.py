from flask import Flask, jsonify, request
from flask_cors import CORS
from gssutils import Scraper
from gssutils.scrape import MetadataError
from markdown import markdown

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    landingPage = request.args.get('landingPage')
    try:
        scraper = Scraper(landingPage)
        return markdown(scraper._repr_markdown_())
    except Exception as err:
        error_type = {
            NotImplementedError: 'Not Implemented',
            MetadataError: 'Metadata Error',
        }.get(type(err), 'Error')
        return markdown(f"# {error_type}\n\n{err}")