from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apple = int(request.form['apple'])
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    name = request.form['first_name']

    print(f" {name} has purchased {apple + raspberry + strawberry} pieces of fruit!")
    print(request.form['apple'])
    return render_template("checkout.html", strawberry = request.form['strawberry'], raspberry = request.form['raspberry'], apple = request.form['apple'], first_name = request.form['first_name'], last_name = request.form['last_name'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)