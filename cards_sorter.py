from test_data import TEST_DATA


class CardsSorter:
    def __init__(self, input_data):
        self.input_data = input_data['cards']
        self.cache = {}
        self.output = []
        self.error = None

    def _create_cache(self):
        for index, card in enumerate(self.input_data):
            self._add_item_to_cache(card["from"], "from", index)
            self._add_item_to_cache(card["to"], "to", index)

    def _add_item_to_cache(self, city_name, direction_key, card_id):
        if city_name not in self.cache:
            self.cache[city_name] = {}
            self.cache[city_name]["count"] = 0
        if direction_key not in self.cache[city_name]:
            self.cache[city_name][direction_key] = card_id
            self.cache[city_name]["count"] += 1
        else:
            raise Exception(f"There are two cards with {city_name} as {direction_key}")

    def _get_trip_start(self):
        trip_start_card_id = None
        trip_end_card_id = None
        for item in self.cache:
            trip_start_card_id = self._validate(self.cache[item], trip_start_card_id, "from")
            trip_end_card_id = self._validate(self.cache[item], trip_end_card_id, "to")
        return trip_start_card_id

    def _validate(self, cache_item, trip_start_or_end, direction_key):
        if cache_item["count"] == 1 and direction_key in cache_item:
            if trip_start_or_end is None:
                return cache_item[direction_key]
            else:
                city_1 = self.input_data[trip_start_or_end][direction_key]
                city_2 = self.input_data[cache_item[direction_key]][direction_key]
                raise Exception(
                    f"There are two candidates for journey {direction_key}: {city_1} and {city_2}")
        else:
            return trip_start_or_end

    def sort(self, card_id):
        for _ in self.input_data:
            self.output.append(self.input_data[card_id])
            city_to = self.input_data[card_id]['to']
            if "from" in self.cache[city_to]:
                card_id = self.cache[city_to]['from']

    def process_cards(self):
        try:
            self._create_cache()
            card_id = self._get_trip_start()
            self.sort(card_id)
        except Exception as err:
            self.error = err.args[0]

    def get_sorted_cards(self):
        return {"cards": self.output}


if __name__ == '__main__':
    cards_sorter = CardsSorter(TEST_DATA)
    cards_sorter.process_cards()
    print(cards_sorter.get_sorted_cards())
