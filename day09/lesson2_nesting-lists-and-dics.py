dictionary = {
  "key": "value1",
  "key": "value2",
  "key": [list],
  "key": {dict},
}

# simple dictionary
cities = {
  "Kenya": "Nairobi",
  "Tanzania": "Dar Es Salaam",
  "Uganda": "Kampala"
}

# Nesting a list in a dictionary
travel_log_list = {
  "Kenya": ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Thika"]
}
print(travel_log_list)

# nesting a dictionary in a dictionary
travel_log = {
  "Kenya": {
    "cities_visited": ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Thika"], "last_visited": 2009
  },
  "Europe": {
    "countries_to_visit": ["Sweden", "Switzerland", "Norway", "Amsterdam"], "next_trip": 2026
  },
}
print(travel_log)

# Nesting a dictionary in a list
travel_log = [
  {
    "country": "Kenya",
    "cities_visited": ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Thika"],
    "last_visited": 2009
    },
  {
    "continent": "Europe",
    "countries_to_visit": ["Sweden", "Switzerland", "Norway", "Amsterdam"],
    "next_trip": 2026
    },
]