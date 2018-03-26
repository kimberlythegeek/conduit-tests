import json

import pytest
import requests
from phabricator import Phabricator

import credentials

api_url_base = "https://phabricator-dev.allizom.org/api/"

def pprint(input):
    print(json.dumps(input, indent=4, sort_keys=True))

def test_get_diff():
    phab = Phabricator(host=api_url_base, token=credentials.api_key)
    response = phab.differential.getdiff(diff_id="178")
    parsed = response.__dict__

    filename = 'diff.json'
    if filename:
        with open(filename, 'r') as f:
            data = json.load(f)
    assert parsed == data

def test_get_raw_diff():
    phab = Phabricator(host=api_url_base, token=credentials.api_key)
    response = phab.differential.getrawdiff(diffID="178")
    parsed = response.__dict__
    with open('rawdiff.json', 'w') as outfile:
        json.dump(parsed, outfile)

    filename = 'rawdiff.json'
    if filename:
        with open(filename, 'r') as f:
            data = json.load(f)
    assert parsed == data
