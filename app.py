from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route('/homepage')
def landing_page():
    return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
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
        return redirect("/registration")

# def login():



if __name__ == "__main__":
    app.run(debug=True)
    
