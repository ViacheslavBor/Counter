from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if not 'counter' in session:
		session['counter'] = 0
	else:
		session['counter'] += 1
	return render_template("index.html")

@app.route('/increment', methods=['POST'])
def increment():	
	if 'counter' in session:
		session['counter'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	if 'counter' in session:
		session['counter'] = 0		
	return redirect('/')
	
app.run(debug=True)