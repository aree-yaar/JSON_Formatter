from formatter_util import beautify_json, minify_json, download_file

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        input_text = request.form['input-text']
        if request.form['action'] == 'format':
            return render_template("home.html", output = beautify_json(input_text, 4), input = input_text)
        elif request.form['action'] == 'minify':
            return render_template("home.html", output = minify_json(input_text), input = input_text)
        else:
            if request.form['output-text']:
                return download_file(request.form['output-text'])
            return render_template('home.html', input=input_text)
    return render_template('home.html', placeholder_input_text = 'Enter your json here')    


if __name__ == "__main__":
    app.run(debug = True)
