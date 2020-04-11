from test_data import TEST_DATA

class CardsSorter:
    def __init__(self, input_data):
        self.input_data = input_data['cards']
        self.cache = {}
        self.output = []
        self.error = None

    def _create_cache(self):
        try:
            for index, card in enumerate(self.input_data):
                self._add_item_to_cache(card["from"], "from", index)
                self._add_item_to_cache(card["to"], "to", index)
        except Exception as err:
            self.error = {"error": err}
            return

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
        self._create_cache()
        if self.error:
            return
        trip_start = None
        trip_end = None
        try:
            for item in self.cache:
                trip_start = CardsSorter._validate(self.cache[item], trip_start, "from")
                trip_end = CardsSorter._validate(self.cache[item], trip_end, "to")
        except Exception as err:
            self.error = {"error": err}
        return trip_start

    @staticmethod
    def _validate(cache_item, trip_start_or_end, direction_key):
        if cache_item["count"] == 1 and direction_key in cache_item:
            if trip_start_or_end is None:
                return cache_item[direction_key]
            else:
                raise Exception(
                    f"There are two candidates for journey {direction_key}: {trip_start_or_end} and {cache_item[direction_key]}")
        else:
            return trip_start_or_end

    def sort(self):
        if self.error:
            return
        card_id = int(self._get_trip_start())
        for _ in self.input_data:
            self.output.append(self.input_data[card_id])
            city_to = self.input_data[card_id]['to']
            if "from" in self.cache[city_to]:
                card_id = self.cache[city_to]['from']

    def get_sorted_cards(self):
        return {"cards": self.output}

cards_sorter = CardsSorter(TEST_DATA)
cards_sorter.sort()
print(cards_sorter.get_sorted_cards())
