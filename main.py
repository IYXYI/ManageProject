from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials for testing purposes (you can later replace this with a database)
USER_CREDENTIALS = {'username': 'admin', 'password': 'password123'}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Check if credentials match
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            return redirect(url_for("index"))  # Redirect to the home page on success
        else:
            return render_template("login.html", error="Invalid credentials, please try again.")
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
