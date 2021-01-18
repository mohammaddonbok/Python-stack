from flask import Flask , render_template
app = Flask(__name__)   

@app.route('/')          
def message():
    return "insert play with any number in the Url"

@app.route('/play')
def draw_box():
    return render_template("play.html",num= 3 , color = "blue")


@app.route('/play/<num>')
def draw_box2(num):
    return render_template("play.html",num=int(num), color = "blue")

@app.route('/play/<num>/<color>')
def draw_box3(num,color):
    return render_template("play.html",num=int(num), color = color)


if __name__=="__main__":
    app.run(debug=True)  