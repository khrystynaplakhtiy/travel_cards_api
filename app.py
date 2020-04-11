from flask import Flask, jsonify
from flask import make_response

app = Flask(__name__)

@app.route('/api/process/v1.0/', methods=['POST'])
def process_api():
    return "response placeholder"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)