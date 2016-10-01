from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def login():
    access_token = request.args.get('token')
    return access_token

if __name__ == '__main__':
    app.run()