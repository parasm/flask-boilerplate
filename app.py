from flask import Flask, render_template, request, redirect
import jinja2
import os

#making a new Flask app
app = Flask(__name__)

#@app.route binds a function to specific url
@app.route('/')
#this function tells the app what to do when it loads the main page
def hello():
	#render_template will render the index.html found in the template folder
	return render_template("index.html")

@app.route('/change')
def change():
	#returning redirect will cause it do go to the specificed URL
	return redirect('/')

#in this app.route we allow POST requests to be sent to /post
@app.route('/post', methods=['GET','POST'])
def post():
	#here we are checking if the request coming in is a post request
	if request.method == 'POST':
		return render_template('post.html')
	#this will run when the user simply goes to the URL
	return render_template('get.html')

if __name__ == '__main__':
	#this code starts the web app, it can be found at http://localhost:8000
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)