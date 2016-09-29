from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def loginpage():
	print stivenprint 
	print request.form 
	return render_template('submit.html')

@app.route("/authenticate", methods = ["POST"])
def authenticate():
	if (requent.form['name'] == 'cry') and (requent.form['pass'] == 'die')
		message = 'Success!!!!'
	else: 
		message = "YOU FAILED AS ALWAYS"
	return render_template('mess.html', val = message)
if __name__ == '__main__':
    app.debug = True
    app.run()