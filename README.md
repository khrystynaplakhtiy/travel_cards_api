# Travel Cards API
### **Run the app**
`docker build -t travel_cards_docker:latest .`
`docker run -d -p 5000:5000 travel_cards_docker:latest`

### **Run the tests**
`docker exec -it CONTAINER ID /bin/bash`
`pytest`

# API Reference
The REST API to the travel cards app is described below

### **Get sorted travel cards**
`POST`
`http://127.0.0.1:5000/api/v1.0/sort`

Success sample request json:
```{
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "connection_number": "SJHA35",
         "seat": "45B",
         "extra_data": "Collect your baggage from station #4"},
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
```

Success sample response json:
```{
  "cards": [
    {
      "connection_number": "",
      "extra_data": "",
      "from": "Los Angeles",
      "seat": "11",
      "to": "Dubai",
      "transport_type": "plane"
    },
    {
      "connection_number": "ALK28",
      "extra_data": "",
      "from": "Dubai",
      "seat": "22B",
      "to": "London",
      "transport_type": "plane"
    },
    {
      "connection_number": "743",
      "extra_data": "",
      "from": "London",
      "seat": "",
      "to": "Berlin",
      "transport_type": "car"
    },
    {
      "connection_number": "SJHA35",
      "extra_data": "Collect your baggage from station #4",
      "from": "Berlin",
      "seat": "45B",
      "to": "Warsaw",
      "transport_type": "plane"
    }
  ],
  "message": [
    "1. Take plane from Los Angeles to Dubai. Take seat #11. ",
    "2. Take plane ALK28 from Dubai to London. Take seat #22B. ",
    "3. Take car 743 from London to Berlin. No seat assignment. ",
    "4. Take plane SJHA35 from Berlin to Warsaw. Take seat #45B. Collect your baggage from station #4",
    "5. Your reached your final destination."
  ]
}
```

Fail sample request json:
```{"cards": [
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
```
Fail sample response json:
```{
  "error": "400 Bad Request: There are two cards with Berlin as from"
}
```





