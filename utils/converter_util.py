import pandas as pd
import json
import yaml
import dicttoxml
from xml.dom.minidom import parseString

def toCSV(input_json):
    info = json.loads(input_json)
    df = pd.json_normalize(info)
    return df.to_csv(index=False)

def toYaml(input_json):
    python_dict = json.loads(input_json)
    yaml_string = yaml.dump(python_dict)
    return yaml_string

def toXML(input_json):
    xml =  dicttoxml.dicttoxml(json.loads(input_json), return_bytes = False, attr_type=False)
    return parseString(xml).toprettyxml()