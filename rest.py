'''
A REST API for docfinder.
'''

from libs import bottle
import json
import docfinder
import subprocess

@bottle.route('/')
def index():
    return 'Welcome to Docfinder!'

# http://localhost:8080/docfinder/v1/search?q=zip,barry
@bottle.get('/docfinder/v1/search')
def search():
    keywords = filter(None, bottle.request.query.get('q', '').split(','))
    results = docfinder.search(*keywords)
    bottle.response.content_type = 'application/json'
    return json.dumps(results, indent=2)

# http://localhost:8080/docfinder/v1/document/pep-3000
@bottle.get('/docfinder/v1/document/<uri>')
def select(uri):
    data = {'uri': uri}
    try:
        text = docfinder.get_document(uri)
    except docfinder.UnknownURI:
        data['status'] = 'error'
        data['error'] = 'UnknownURI'
    else:
        data['status'] = 'OK'
        data['content'] = text
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

# http://localhost:8080/docfinder/v1/document/pep-3000
@bottle.post('/docfinder/v1/document/<uri>')
def insert(uri):
    text = bottle.request.POST.get('text', '')
    data = {'uri': uri, 'text': text}
    try:
        docfinder.add_document(uri, text)
    except docfinder.DuplicateURI:
        data['status'] = 'error'
        data['error'] = 'DuplicateURI'
    else:
        data['status'] = 'OK'
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

# SCARY!!! Do not use this for untrusted users
@bottle.get('/cmd/v1/<command>')
def execute(command):
    argv = command.split()
    try:
        output = subprocess.check_output(argv)
    except Exception as e:
        data = {'status': 'error',
                'error': str(e)}
    else:
        data = {'status': 'OK', 'output': output}
    return json.dumps(data, indent=2)
    
if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
