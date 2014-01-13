from flask import Flask, request
from flask import render_template

import datetime
app = Flask(__name__)

@app.route("/")
def home():
	return "Hello World! <a href='dashboard'>Next page</a>"

@app.route('/dashboard/<username>')
def hello(username=None):
	return render_template('dashboard.html', title="Dashboard")

@app.route('/<month>/<day>/<year>/<title_slug>')
def api(month=0, day=0, year=0, title_slug=None):
	date = None
	try:
		date = datetime.date(year, month, day)
	except ValueError:
		date = datetime.date( 2014, 1, 1 )

	return render_template('api.html', date=date)



if __name__ == '__main__':
	app.debug = True
	app.run()