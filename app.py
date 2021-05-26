from flask import Flask
from flask import request
from flask.helpers import send_file
import io
import os
import signal
import logging
import pandas as pd

app = Flask(__name__)
import indeed_job_scraper, linkedin_job_scraper


# @app.route("/")
# def hello():
#     return "Hello, World!"
@app.route("/", methods=['GET', 'POST'])
def scraper():
    # if request.method == 'GET':
    #     return 'hello'
    # else:
        type = request.args.get('type')
        title = request.args.get('title')
        loc = request.args.get('loc')
        if type == 'indeed':
            indeed_job_scraper.main(title, loc, 'indeed_results.xlsx')
            return download_file('indeed_results.xlsx')
        if type == 'linkedin':
            linkedin_job_scraper.main(title, loc, 'linkedin_results.xlsx')
        return 'success'


def download_file(file):
    # global_df = pd.DataFrame([])
    # # # Convert DF to memory stream
    # strIO = io.BytesIO()
    # excel_writer = pd.ExcelWriter(strIO, engine="xlsxwriter",options={'strings_to_urls': False})
    # global_df.to_excel(excel_writer, sheet_name="Jobs",index=False)
    # excel_writer.save()
    # excel_data = strIO.getvalue()
    # strIO.seek(0)

    return send_file(os.path.join('.', file))

