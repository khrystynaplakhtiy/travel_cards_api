from flask import Flask, jsonify, request, abort
from flask import make_response
from cards_sorter import CardsSorter

app = Flask(__name__)

@app.route('/api/sort/v1.0/', methods=['POST'])
def process_api():
    cards_sorter = CardsSorter(request.json)
    cards_sorter.sort()
    if cards_sorter.error:
        abort(400, cards_sorter.error)
    else:
        return make_response(jsonify(cards_sorter.get_sorted_cards()), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_data(error):
    return make_response(jsonify({'error': str(error)}), 400)


if __name__ == '__main__':
    app.run(debug=True)
