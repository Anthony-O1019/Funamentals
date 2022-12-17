from crypt import methods
import re
from flask import Flask, render_template, request, session, redirect, request
app = Flask(__name__)

app.secret_key="Secrets stay Secrets"

@app.route('/')
def task1():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def task2():
    session['name'] = request.form['name']
    session['home'] = request.form['home']
    session['list'] = request.form['list']
    session['comment'] = request.form['comment']

    return redirect('/success')

@app.route('/success')
def task3():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True)