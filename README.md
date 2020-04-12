# Travel Cards API
### **Install**


### **Run the app**
`python app.py`

### **Run the tests**
`pytest`

# API Reference
The REST API to the travel cards app is described below

### **Get sorted travel cards**
`POST`
`http://127.0.0.1:5000/api/v1.0/sort/`

Success sample request json:
```{
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "to": "London",
         "transport_type": "plane",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Berlin",
         "transport_type": "car",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "seat": "11",
         "extra_data": ""}
    ]
}
```

Success sample response json:
```{
  "cards": [
    {
      "extra_data": "",
      "from": "Los Angeles",
      "seat": "11",
      "to": "Dubai",
      "transport_type": "plane"
    },
    {
      "extra_data": "",
      "from": "Dubai",
      "seat": "22B",
      "to": "London",
      "transport_type": "plane"
    },
    {
      "extra_data": "",
      "from": "London",
      "seat": "",
      "to": "Berlin",
      "transport_type": "car"
    },
    {
      "extra_data": "",
      "from": "Berlin",
      "seat": "45B",
      "to": "Warsaw",
      "transport_type": "plane"
    }
  ]
}
```

Fail sample request json:
```{
    "cards": [
        {"from": "Berlin",
         "to": "Warsaw",
         "transport_type": "plane",
         "seat": "45B",
         "extra_data": ""},
        {"from": "Dubai",
         "to": "London",
         "transport_type": "plane",
         "seat": "22B",
         "extra_data": ""},
        {"from": "London",
         "to": "Berlin",
         "transport_type": "car",
         "seat": "",
         "extra_data": ""},
        {"from": "Los Angeles",
         "to": "Dubai",
         "transport_type": "plane",
         "seat": "11",
         "extra_data": ""},
			  {"from": "lviv",
         "to": "kyiv",
         "transport_type": "plane",
         "seat": "11",
         "extra_data": ""}
    ]
}
```
Fail sample response json:
```{
  "error": "400 Bad Request: There are two candidates for journey from: Los Angeles and lviv"
}
```





