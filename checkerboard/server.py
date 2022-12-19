from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def check():
    return render_template("index.html", rows=2, columns=2, color1="red", color2="blue")

@app.route('/<rows>/<columns>')

def check2(rows,columns):
    return render_template("index.html", rows=int(rows), columns=int(columns), color1="red", color2="blue")

@app.route('/<rows>/<columns>/<string:color1>/<string:color2>')

def check3(rows,columns, color1, color2):
    return render_template("index.html", rows=int(rows), columns=int(columns), color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)