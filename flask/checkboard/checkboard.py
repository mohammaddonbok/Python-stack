from flask import Flask , render_template
app = Flask(__name__)   

@app.route('/')          
def display_8():
    check_width=60*8
    check_height=60*8
    return render_template("checkboard.html",x=8 ,y=8,c1= "red",c2="black",  check_width=check_width , check_height=check_height)

@app.route('/<int:num>')          
def display_4(num):
    check_width=60*8
    check_height=(60*num)
    return render_template("checkboard.html",x=8 ,y=num,c1= "red",c2="black",  check_width=check_width , check_height=check_height)

@app.route('/<int:num1>/<int:num2>')          
def display(num1,num2):
    check_width=(60*num1)
    check_height=(60*num2)
    return render_template("checkboard.html",x=num1 ,y=num2,c1= "red",c2="black",  check_width=check_width , check_height=check_height)

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')          
def display_with_color(num1,num2,color1,color2):
    check_width=(60*num1)
    check_height=(60*num2)
    return render_template("checkboard.html",x=num1 ,y=num2,c1= color1,c2=color2,  check_width=check_width , check_height=check_height)
if __name__=="__main__":
    app.run(debug=True)  
