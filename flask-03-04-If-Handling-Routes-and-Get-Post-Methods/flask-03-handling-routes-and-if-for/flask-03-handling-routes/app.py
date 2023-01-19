from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello from Flask 03</h1>"


@app.route("/greet")
def greet():
    return render_template("greet.html", name="ambika")

@app.route("/evens")
def evens():
    return render_template("evens.html")    

@app.route("/list")
def showList10():
    return render_template("list10.html")

@app.route("/google")
def google():
    return redirect("https://www.google.com") #this redirects to the google url

@app.route("/error")
def error():
    return '<h1 style="color:red">Error prohibited </h1>'

@app.route("/admin")
def admin():
    return redirect(url_for("error"))     #this is redirecting to the above route error    







if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 3000, debug=False)
