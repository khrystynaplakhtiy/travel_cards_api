from flask import Flask, jsonify, request, abort
from flask import make_response
from cerberus import Validator
from cards_sorter import CardsSorter

app = Flask(__name__)


def validate_json(document):
    schema = {
        'cards': {
            'type': 'list', 'schema': {
                'type': 'dict', 'schema': {
                    'from': {'type': 'string', 'required': True},
                    'to': {'type': 'string', 'required': True},
                    'transport_type': {'type': 'string', 'required': True},
                    'connection_number': {'type': 'string', 'required': True},
                    'seat': {'type': 'string', 'required': True},
                    'extra_data': {'type': 'string', 'required': True}
                }
            }
        }
    }
    v = Validator(schema)
    return v.validate(document, schema)


@app.route('/api/v1.0/sort', methods=['POST'])
def process_api():
    req = request.json
    if not validate_json(req):
        abort(400, "Wrong json structure")
    cards_sorter = CardsSorter(req)
    cards_sorter.process_cards()
    if cards_sorter.error:
        abort(400, cards_sorter.error)
    else:
        return make_response(jsonify(cards_sorter.get_sorted_cards_and_message()), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_data(error):
    return make_response(jsonify({'error': str(error)}), 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
