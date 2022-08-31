import os
import json
from flask import Flask, render_template, flash # importing Flask class and render template function from Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__) # creating an instance of the class and storing in app variable. First argument of Flask class is the name of the apps module - our package.  Flask needs to know where to look for templates and static files. 
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/") # app route decorator - starts with @ - way of wrapping functions.
def index(): #root decorator binds index function to itself so whenever that root is called, the function is called.
    return render_template("index.html") # function is also called a view.


@app.route("/about")
def about():
    data= []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3], company=data)

@app.route("/about/<member_name>") # angle brackets pass in the member url data
def about_member(member_name): 
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
    
@app.route("/contact")
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": # __main__ is the name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")), #5000 is common port used by Flask
        debug=True) # Should never have debug=true in production environment or submitted projects 