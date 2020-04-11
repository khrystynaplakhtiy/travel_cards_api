from test_data import TEST_DATA


class CardsSorter:
    def __init__(self, input_data):
        self.input_data = input_data
        self.cache = {}
        self.output = {}

    def _create_cache(self):
        for index, card in enumerate(self.input_data["cards"]):
            self._add_item_to_cache(card["from"], "from", index)
            self._add_item_to_cache(card["to"], "to", index)

    def _add_item_to_cache(self, city_name, direction, card_id):
        if city_name not in self.cache:
            self.cache[city_name] = {}
            self.cache[city_name]["count"] = 0

        if direction not in self.cache[city_name]:
            self.cache[city_name][direction] = card_id
            self.cache[city_name]["count"] += 1
        else:
            raise Exception(f"There are two cards with {city_name} as {direction}")

    def _get_start(self):
        self._create_cache()
        start = None
        end = None
        for item in self.cache:
            start = CardsSorter._validate(self.cache[item], start, "from")
            end = CardsSorter._validate(self.cache[item], end, "to")
        return start

    @staticmethod
    def _validate(item, direction, direction_key):
        if item["count"] == 1 and direction_key in item:
            if direction is None:
                return item[direction_key]
            else:
                raise Exception(
                    f"There are two candidates for journey {direction_key}: {direction} and {item[direction_key]}")
        else:
            return direction




cards_sorter = CardsSorter(TEST_DATA)
print(cards_sorter._get_start())
