# -*- coding: utf-8 -*-
from html import unescape
import requests
import json

def unesc(ob) -> object:
    if isinstance(ob, list):
        return [unesc(v) for v in ob]
    elif isinstance(ob, dict):
        return {k: unesc(v) for k, v in ob.items()}
    elif isinstance(ob, str):
        return unescape(ob)
    return ob

url = 'http://glosbe.com/gapi/translate'

params={'from':'fra', 'dest':'eng', 'format':'json', 'pretty': 'false', 'callback': 'glosbe', 'phrase': ''}
def glosbe(word):
    params['phrase'] = word
    resp = requests.get(url, params=params)
    # gbd = unesc(resp.json())
    gdbjs = resp.text[7:-2]
    # print(gdbjs)
    gbd = json.loads(gdbjs )
    gdb = unesc(gbd)
    if gbd['result'] == 'ok':
        defs = [defn['phrase']['text'] for defn in gbd['tuc'] if 'phrase' in defn]
        # print(word, defs)
        return defs

if __name__ == '__main__':
    print(glosbe('chat'))