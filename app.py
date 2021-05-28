from flask import Flask
from flask import request
from flask.helpers import send_file
from flask_cors import CORS, cross_origin
import indeed_job_scraper
import linkedin_job_scraper

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/hello")
def hello():
    return "Hello, World!"


@cross_origin(origin='*')
@app.route("/", methods=['GET', 'POST'])
def scraper():
    domain = request.args.get('domain')
    date_posted = request.args.get('date_posted')
    title = request.args.get('title')
    loc = request.args.get('loc')
    linkedin_job_scraper.main("linkedin.com", date_posted, title, loc, 'results.xlsx')
    indeed_job_scraper.main("ae.indeed.com", date_posted, title, loc, 'results.xlsx')

    return download_file(title)


def download_file(title):
    return send_file('results.xlsx', as_attachment=True)
