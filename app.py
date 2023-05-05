from flask import Flask, render_template, request, url_for, redirect
import json
app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        input_text = request.form['input-text']
        output_text = json.dumps(json.loads(input_text), indent = 4)
        return render_template("home.html", output = output_text, input = input_text) 
    return render_template('home.html', output = 'Placeholder text')    


if __name__ == "__main__":
    app.run(debug = True)