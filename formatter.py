import json

def beautify_json(input_text, indentation):
    return json.dumps(json.loads(input_text), indent = indentation)
