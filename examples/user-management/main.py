from flask import Flask, request, jsonify
app = Flask(__name__)

users = [{
    'username': 'test1',
    'password': 'test1',
    'id': '1'
}, {
    'username': 'test2',
    'password': 'test2',
    'id': '2'
}, {
    'username': 'test3',
    'password': 'test3',
    'id': '3'
}]


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if (data['username'] == user['username']
                and data['password'] == user['password']):
            return jsonify({'identity': user['id']})
    return (''), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
