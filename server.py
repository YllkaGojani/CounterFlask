from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def count():
	if session['times'] >= 1:
		session['times'] += 1
	else:
		session['times'] = 1		
	return render_template("index.html",times = session['times'])	

@app.route('/+2',methods=['POST'])
def add():
	session['times'] += 1
	return redirect('/')	

@app.route('/beginAgain',methods=['POST'])
def beginAgain():
		session['times'] = 1
		return redirect('/')

app.run(debug=True)	