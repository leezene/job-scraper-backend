from flask import Flask
from flask import request
from flask.helpers import send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import indeed_job_scraper, linkedin_job_scraper


@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/", methods=['GET', 'POST'])
def scraper():
    # if request.method == 'GET':
    #     return 'hello'
    # else:
    type = request.args.get('type')
    title = request.args.get('title')
    loc = request.args.get('loc')
    if type == 'indeed':
        indeed_job_scraper.main(title, loc, 'results.xlsx')
    if type == 'linkedin':
        linkedin_job_scraper.main(title, loc, 'results.xlsx')
    return download_file(title)


def download_file(title):
    return send_file('results.xlsx', as_attachment=True)
