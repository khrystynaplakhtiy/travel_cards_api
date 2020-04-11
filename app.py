from flask import Flask, jsonify, request
from flask import make_response
import CardSorter

app = Flask(__name__)

@app.route('/api/process/v1.0/', methods=['POST'])
def process_api():
    card_sort = CardSorter(request.json)
    card_sort.sort()
    if card_sort.error:
        bad_data(card_sort.error)
    else:
        return make_response(card_sort.output, 200)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_data(error):
    return make_response(jsonify({'error': error}), 400)

if __name__ == '__main__':
    app.run(debug=True)