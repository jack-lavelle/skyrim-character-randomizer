import json


def read_json_as_dict(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)
