# -*- coding: utf-8 -*-
import urllib.request
import json
import html

url = ' http://glosbe.com/gapi/translate?from=fra&dest=eng&format=json&phrase={}&pretty=true'

def unescape_entities(value):
    return html.unescape(value)

def process(ob):
    if isinstance(ob, list):
        return [process(v) for v in ob]
    elif isinstance(ob, dict):
        return {k: process(v) for k, v in ob.items()}
    elif isinstance(ob, str):
        return unescape_entities(ob)
    return ob

def getdef(word):

    escword = html.escape(word)
    weburl = urllib.request.urlopen(url.format(escword))
    data = weburl.read().decode('utf-8')

    theJSON = json.loads(data)
    print(theJSON)

    theJSON = process(theJSON)
    print(theJSON)

getdef('fère')