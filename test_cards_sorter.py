from cards_sorter import CardsSorter
from test_data import TEST_DATA, TEST_DATA_DUPLICATE_END, TEST_DATA_DUPLICATE_FROM, \
    TEST_DATA_DUPLICATE_TO, TEST_DATA_DUPLICATE_START

import pytest


def test_create_cache_success():
    cards_sorter = CardsSorter(TEST_DATA)
    cards_sorter._create_cache()
    expected_cache = {'Berlin': {'count': 2, 'from': 0, 'to': 2}, 'Warsaw': {'count': 1, 'to': 0},
                      'Dubai': {'count': 2, 'from': 1, 'to': 3}, 'London': {'count': 2, 'to': 1, 'from': 2},
                      'Los Angeles': {'count': 1, 'from': 3}}
    assert cards_sorter.cache == expected_cache


@pytest.mark.parametrize('test_data, exception_message',
                         [
                             (TEST_DATA_DUPLICATE_FROM, "There are two cards with Berlin as from"),
                             (TEST_DATA_DUPLICATE_TO, "There are two cards with Warsaw as to")
                         ])
def test_create_cache_fail(test_data, exception_message):
    cards_sorter = CardsSorter(test_data)
    with pytest.raises(Exception) as e:
        cards_sorter._create_cache()
    assert str(e.value) == exception_message


def test_get_trip_start_success():
    cards_sorter = CardsSorter(TEST_DATA)
    cards_sorter._create_cache()
    assert cards_sorter._get_trip_start() == 3


@pytest.mark.parametrize('test_data, exception_message',
                         [
                             (TEST_DATA_DUPLICATE_START,
                              "There are two candidates for journey from: New York and Los Angeles"),
                             (TEST_DATA_DUPLICATE_END, "There are two candidates for journey to: Warsaw and Berlin")
                         ])
def test_get_trip_start_fail(test_data, exception_message):
    cards_sorter = CardsSorter(test_data)
    cards_sorter._create_cache()
    with pytest.raises(Exception) as e:
        cards_sorter._get_trip_start()
    assert str(e.value) == exception_message


def test_sort_success():
    cards_sorter = CardsSorter(TEST_DATA)
    cards_sorter._create_cache()
    card_id = cards_sorter._get_trip_start()
    cards_sorter._sort(card_id)

    expected_output = [
        {'from': 'Los Angeles', 'to': 'Dubai', 'transport_type': 'plane', "connection_number": "", 'seat': '11',
         'extra_data': ''},
        {'from': 'Dubai', 'to': 'London', 'transport_type': 'plane', "connection_number": "ALK28", 'seat': '22B',
         'extra_data': ''},
        {'from': 'London', 'to': 'Berlin', 'transport_type': 'car', "connection_number": "743", 'seat': '',
         'extra_data': ''},
        {'from': 'Berlin', 'to': 'Warsaw', 'transport_type': 'plane', "connection_number": "SJHA35", 'seat': '45B',
         'extra_data': ''}]

    assert expected_output == cards_sorter.output


@pytest.mark.parametrize('test_data, exception_message',
                         [
                             (TEST_DATA_DUPLICATE_START,
                              "There are two candidates for journey from: New York and Los Angeles"),
                             (TEST_DATA_DUPLICATE_END, "There are two candidates for journey to: Warsaw and Berlin"),
                             (TEST_DATA_DUPLICATE_FROM, "There are two cards with Berlin as from"),
                             (TEST_DATA_DUPLICATE_TO, "There are two cards with Warsaw as to")

                         ])
def test_process_cards_errors(test_data, exception_message):
    cards_sorter = CardsSorter(test_data)
    cards_sorter.process_cards()

    assert cards_sorter.error == exception_message
