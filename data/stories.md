## search cards
* greet
  - utter_greet
* search{"product": "card"}
  - slot{"product": "card"}
  - utter_ok_search_cards
* goodbye
  - utter_goodbye

## search sets
* greet
  - utter_greet
* search{"product": "set"}
  - slot{"product": "set"}
  - utter_ok_search_sets
* goodbye
  - utter_goodbye

## search by prompting, cards
* greet
  - utter_greet
* search
  - utter_search_what
* search{"product": "card"}
  - slot{"product": "card"}
  - utter_ok_search_cards
* goodbye
  - utter_goodbye

## search by prompting, sets
* greet
  - utter_greet
* search
  - utter_search_what
* search{"product": "set"}
  - slot{"product": "set"}
  - utter_ok_search_sets
* goodbye
  - utter_goodbye
