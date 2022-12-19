from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
import random
app.secret_key = 'Do not look here please'

@app.route('/')
def task1(): 
    if 'random' in session:
        print('key exists!')
    else:
        session['random'] = random.randint(1,100)
        print("key 'random' now exist")
    print(session['random'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def task2():
    session['guess'] = int(request.form['guess'])

    return redirect('/')

@app.route('/reset')
def task3():
    session.pop('random')

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)