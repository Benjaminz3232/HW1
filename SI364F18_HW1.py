## HW 1
## SI 364 F18
## 1000 points

import json
import requests
from flask import Flask, request

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

#None

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello! This is a test and Holly is my best friend ever, she is also my wife but not in the eyes of the law, the law being commander mom :)'

@app.route('/class')
def daclass():
	return "Welcome to SI 364, it is a wonderful time here"


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

@app.route('/movie/<name>')
def movie(name):
	base_url = 'http://itunes.apple.com/search'
	params = {'media':'movie', 'term':name}
	getname = requests.get(base_url, params = params)
	json_format = json.loads(getname.text)
	return getname.text

# # {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

@app.route('/question')
def num_entry():
	n = """<DOCTYPE html>
<html>
<body>
<form action = '/result' method = 'GET'>
<div>
	Enter your favorite number:
	<input type = 'text' name = 'number' value = ''>
	input type = 'submit' value = 'Submit'
<div>
</form> 
</body>
</html>""" 
	return n

@app.route('/result', methods = ['POST', 'GET'])
def thatnumberthang():
	if request.method == 'GET':
		result = request.args
		entered_num = result.get('number')
		new_num = 2*(int(entered_num))
		return "Double your favorite number is {}".format(new_num)

## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.

@app.route('/problem4', methods = ['GET'])
def choose_artist():
	thestuff = """<!DOCTYPE html>
<html>
<body>
<form name="itsmyformbinch" action="/movie" method="get">
<p>
Choose a movie to find out stuff about it <b> <br>
<input type="radio" name="option" value="Sharknado"> Sharknado <br>
<input type="radio" name="option" value="Inception"> Inception <br>
<input type="radio" name="option" value="Alpha"> Alpha <br>
</p>
<p><input type=submit value=Next></p>
</form>
</form> 
</body>
</html>""" 
	return thestuff
#
#
#
#
# really couldn't figure out how to get this part to work. 
# Was confused as to how to call to the user form and use 
# that data to refer to in the code below. I will
# definitely be going to office hours so that I can
# understand this. Hopefully I can be awarded some half
# credit for my efforts.
#
#
#


@app.route('/movie', method = ['GET'])
def movie():
	base_url = 'http://itunes.apple.com/search'
	params = {'media':'movie', 'term':option}
	getname = requests.get(base_url, params = params)
	json_format = json.loads(getname.text)
	return getname.text


# @app.route('/movie')
# def movie():
# 	result = request.args
# 	movie = result.get('option')
# 	base_url = 'http://itunes.apple.com/search?term='
# 	url = base_url + movie
# 	req = requests.get(url, params)

# 	params = {'media':'movie', 'term':name}
# 	getname = requests.get(base_url, params = params)
# 	json_format = json.loads(getname.text)
# 	return getname.text


if __name__ == '__main__':
    app.run()
