from flask import Flask , render_template
app = Flask(__name__)   

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello " + name

@app.route('/repeat/<int:num>/<name>')
def repeat(name , num):
    return render_template("index.html",name=name, num=int(num))

# @app.route('/repeat/<num>/<name>')
if __name__=="__main__":
    app.run(debug=True)