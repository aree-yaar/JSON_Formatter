import pandas as pd
import json
import yaml
from dicttoxml import dicttoxml
import xmltodict
from json2xml import json2xml
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
    return  xmltodict.unparse(json.loads(input_json), full_document=False, pretty = True)