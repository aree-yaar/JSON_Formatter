from flask import Flask, render_template, request, flash
from utils.converter_util import toCSV, toYaml, toXML
from utils.formatter_util import beautify_json, minify_json, download_file, validate_json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=("GET", "POST"))
def home():
    input_text = ""
    if request.method == "POST":
        input_text = request.form['input-text']
        print(request.files)
        if('file' in request.files):
            print(request.files, 1)
            file = request.files['file']
            filename = secure_filename(file.filename)
            print(filename)
            return render_template("home.html", input = "ABCD")

                
        if request.form['converter'] == 'CSV':
            return render_template("home.html", output = toCSV(input_text), input = input_text)
        elif request.form['converter'] == 'YAML':
            return render_template("home.html", output = toYaml(input_text), input = input_text)
        elif request.form['converter'] == 'XML':
            return render_template("home.html", output = toXML(input_text), input = input_text)
        elif request.form['action'] == 'download':
            if request.form['output-text']:
                return download_file(request.form['output-text'])
            else:
                flash('No Output Found', 'danger')
            return render_template('home.html', input=input_text)
        
        else:
            is_json_valid = validate_json(input_text)
            if is_json_valid == True:
                
                if request.form['action'] == 'format':
                    indent = int(request.form['indent'])
                    return render_template("home.html", output = beautify_json(input_text, indent), input = input_text)
                elif request.form['action'] == 'minify':
                    return render_template("home.html", output = minify_json(input_text), input = input_text)
            else:
                flash('INVALID JSON', 'danger')
                
    return render_template('home.html', 
                           placeholder_input_text = 'Enter your json here', 
                           input = input_text, 
                           )


if __name__ == "__main__":
    app.run(debug = True)