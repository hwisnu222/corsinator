from flask import Flask, request, Response
import requests

app = Flask(__name__)

TARGET_URL = 'https://api.example.com/api/v1'

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"{TARGET_URL}/{path}"
    
    if request.method == 'GET':
        resp = requests.get(url, params=request.args)
    elif request.method == 'POST':
        resp = requests.post(url, json=request.json)
    elif request.method == 'PUT':
        resp = requests.put(url, json=request.json)
    elif request.method == 'DELETE':
        resp = requests.delete(url, json=request.json)

    
    response = Response(
        resp.content,
        status=resp.status_code,
        content_type=resp.headers.get('Content-Type')
    )
    
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

    return response

if __name__ == '__main__':
    app.run(port=8080, debug=True)
