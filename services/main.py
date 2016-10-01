from flask import Flask, request
from user import user

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def login():
    access_token = request.args.get('t')
    print(access_token)
    return ""

if __name__ == '__main__':
    app.run()