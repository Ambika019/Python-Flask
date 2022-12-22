from flask import Flask, render_template







app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html", name="Ambika", lastName="Singh")









if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=False)