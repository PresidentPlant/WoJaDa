from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route('/homepage')
def homepage():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        flash("Enter Details to Register")
        return render_template("register.html")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        dob = request.form["dob"]
        password = request.form["password"]
        if name == "" or email == "" or password == "" or dob == "":
            flash("Please fill out the missing fields")
        return redirect("/register")

@app.route("/login", methods=["GET", "POST"])
def login():
    pass


if __name__ == "__main__":
    app.run(debug=True)
    
