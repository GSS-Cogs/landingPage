from flask import Flask, jsonify, request
from flask_cors import CORS
from gssutils import Scraper
from gssutils.scrape import MetadataError
from markdown import markdown
import requests

class MatchingError(Exception):
    """ Raised when an expected (by the front end) partial match does not yield a result
    """

    def __init__(self, message):
        self.message = message

GENERIC_EXCEPTION_HELP = """
If you're seeing this we have a scraper but there's some sort of issue with it, likely causes:\n
- it's broke (i.e page has changed since it was written).\n
- it's too broad (i.e it "thinks" it works on this page, but actually only works in a related one).\n
Because of the latter reason it's worth trying again on nearby/related pages to try and get a hit.\n
Either way can you flag it with the tech team by popping the url onto this github issue please: <a href="https://github.com/GSS-Cogs/gss-utils/issues/67">https://github.com/GSS-Cogs/gss-utils/issues/67</a>, thanks.
"""

app = Flask(__name__)
CORS(app)

def getPartialMatches(landingPage):
    """
    If we have the domain but not a scraper feedback some kind of helpful nudge towards which url(s) would work.
    """
    r = requests.get("https://raw.githubusercontent.com/GSS-Cogs/gss-utils/master/gssutils/scrapers/__init__.py")
    if r.status_code != 200:
        raise Exception("Unable to acquire scraper master list. Status code '{}'.".format(r.status_code))
    
    # Parse out the urls
    urls = []
    for line in r.text.split("\n"):
        if "http://" in line or "https://" in line:
            urls.append(line.split("'")[1].split("'")[0]) # ewww, do it properly

    # Get domain of landing page
    path_segments = landingPage.split("/")
    domain = "/".join(path_segments[:3])

    partial_matches = [x for x in urls if x.startswith(domain)]
    
    # This shouldn't be possible given we only scrape where we have a domain match of some kind
    # though in case of random url formatting issues we'd best catch it.
    if len(partial_matches) == 0:
        return MatchingError("Unable to find the expected partial match for domain '{}' in '{}'." \
            .format(domain, "\n".join(urls)))
    else:
        return """
        \nHowever, we do have the following related scrapers on this domain, would one of these work?
        \n
        {}
        """.format("\n".join(["* "+x.strip() for x in partial_matches]))


@app.route('/')
def index():
    landingPage = request.args.get('landingPage')
    try:
        scraper = Scraper(landingPage)
        return markdown(scraper._repr_markdown_())
    except NotImplementedError as errNotImplemented:
        return markdown(f"# Not Implemented\n\n{errNotImplemented}{getPartialMatches(landingPage)}")
    except MetadataError as errMetadata:
        return markdown(f"# Metadata Error\n\n{errMetadata}")
    except Exception as err:
        return markdown(f"# Error\n\n{err}\n\n{GENERIC_EXCEPTION_HELP}")


if __name__ == "__main__":
    app.run(debug=True)