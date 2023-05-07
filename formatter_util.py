import json

from flask import Response

def beautify_json(input_text, indentation):
    return json.dumps(json.loads(input_text), indent=indentation)

def minify_json(input_text):
    return json.dumps(json.loads(input_text))

def download_file(content):
    return Response(content,
            mimetype="application/json",
            headers={"Content-Disposition":
                    "attachment;filename=JSON_Formatter.txt"})
