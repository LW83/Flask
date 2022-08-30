import os
from flask import Flask, render_template # importing Flask class and render template function from Flask


app = Flask(__name__) # creating an instance of the class and storing in app variable. First argument of Flask class is the name of the apps module - our package.  Flask needs to know where to look for templates and static files. 


@app.route("/") # app route decorator - starts with @ - way of wrapping functions.
def index(): #root decorator binds index function to itself so whenever that root is called, the function is called.
    return render_template("index.html") # function is also called a view.


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__": # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")), #5000 is common port used by Flask
        debug=True) # Should never have debug=true in production environment or submitted projects 