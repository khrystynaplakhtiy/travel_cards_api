import pytest
from app import validate_json
from test_data import REQ_BAD_STRUCTURE_1, REQ_BAD_STRUCTURE_2, REQ_BAD_STRUCTURE_3, REQ_BAD_STRUCTURE_4, \
    REQ_BAD_STRUCTURE_5


@pytest.mark.parametrize('document, expected_result',
                         [
                             (REQ_BAD_STRUCTURE_1, False),
                             (REQ_BAD_STRUCTURE_2, False),
                             (REQ_BAD_STRUCTURE_3, False),
                             (REQ_BAD_STRUCTURE_4, False),
                             (REQ_BAD_STRUCTURE_5, False)
                         ])
def test_validate_json(document, expected_result):
    assert validate_json(document) == expected_result
