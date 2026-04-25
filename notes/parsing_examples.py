# notes/parsing_examples.py
import json
import csv
from io import StringIO

def parse_json_string(s):
    return json.loads(s)

def to_json(obj):
    return json.dumps(obj, indent=2)

def parse_csv_string(s):
    # returns list of dicts assuming header row present
    f = StringIO(s)
    reader = csv.DictReader(f)
    return list(reader)

# small example of using argparse-like behavior without importing argparse
def parse_key_value_args(args):
    # args: ["--name=Alice", "--age=30"]
    result = {}
    for a in args:
        if a.startswith("--") and "=" in a:
            k, v = a[2:].split("=", 1)
            result[k] = v
    return result

if __name__ == "__main__":
    js = '{"name":"Alice","age":30}'
    print("JSON parsed:", parse_json_string(js))
    csv_text = "name,score\nAlice,90\nBob,85"
    print("CSV parsed:", parse_csv_string(csv_text))
    print("KV args:", parse_key_value_args(["--name=Alice","--age=30"]))
