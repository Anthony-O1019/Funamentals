from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Hello!!!'

@app.route('/')
def task1():
    if 'total_views' in session:
        session['total_views'] +=1
    else:
        session['total_views'] = 0
    return render_template('index.html')

@app.route('/reset')
def task2():
    session.pop('total_views')

    return redirect('/')

@app.route('/plus')
def task3():
    if 'total_views' in session:
        session['total_views'] +=1
    else:
        session['total_views'] =0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)