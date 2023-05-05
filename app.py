from flask import Flask, render_template, request
from formatter import beautify_json
app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        input_text = request.form['input-text']
        return render_template("home.html", output = beautify_json(input_text, 4), input = input_text) 
    return render_template('home.html', input = 'Enter your json here')    


if __name__ == "__main__":
    app.run(debug = True)
