from flask import Flask , render_template , redirect , request, session
app=Flask(__name__)

@app.route('/')
def display():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    # return render_template('tabel.html',f=f,l=l,f1=f1,l1=l1,f2=f2,l2=l2)
    return render_template('tabel.html',user=users)
if __name__=="__main__":
    app.run(debug=True)
