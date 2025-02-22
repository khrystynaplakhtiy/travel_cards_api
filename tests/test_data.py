TEST_DATA = {
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": "Collect your baggage from belt #4"},
        {"from": "Dubai",
         "to": "London",
         "transport_type": "plane",
         "connection_number": "ALK28",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Berlin",
         "transport_type": "car",
         "connection_number": "743",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "connection_number": "",
         "seat": "11",
         "extra_data": ""}
    ]
}

TEST_DATA_DUPLICATE_FROM = {
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Berlin",
         "to": "London",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Berlin",
         "transport_type": "car",
         "connection_number": "SJHA35",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "11",
         "extra_data": ""}
    ]
}

TEST_DATA_DUPLICATE_TO = {
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "to": "London",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Warsaw",
         "transport_type": "car",
         "connection_number": "SJHA35",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "11",
         "extra_data": ""}
    ]
}

TEST_DATA_DUPLICATE_END = {
    "cards": [
        {"from": "New York",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "to": "London",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Berlin",
         "transport_type": "car",
         "connection_number": "SJHA35",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "11",
         "extra_data": ""}
    ]
}

TEST_DATA_DUPLICATE_START = {"cards": [
    {"from": "New York",
     "to": "Warsaw",
     "transport_type": "plane",
     "connection_number": "SJHA35",
     "seat": "45B",
     "extra_data": ""},
    {"from": "Los Angeles",
     "to": "Dubai",
     "transport_type": "plane",
     "connection_number": "SJHA35",
     "seat": "11",
     "extra_data": ""},
    {"from": "Dubai",
     "to": "London",
     "transport_type": "plane",
     "connection_number": "SJHA35",
     "seat": "22B",
     "extra_data": ""},
    {"from": "London",
     "to": "Berlin",
     "transport_type": "car",
     "connection_number": "SJHA35",
     "seat": "",
     "extra_data": ""}

]
}

REQ_BAD_STRUCTURE_1 = {
    "key": "value"
}

REQ_BAD_STRUCTURE_2 = {
    "cards": "value"
}

REQ_BAD_STRUCTURE_3 = {
    "cards": ["string 1", "string 2"]
}

REQ_BAD_STRUCTURE_4 = {
    "cards": [
        {"to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "22B",
         "extra_data": ""}
    ]
}

REQ_BAD_STRUCTURE_5 = {
    "cards": [
        {"from": "Dubai",
         "from": "Lviv",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "22B",
         "extra_data": ""}
    ]
}
