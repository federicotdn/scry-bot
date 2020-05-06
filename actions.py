from typing import Any, Text, Dict, List, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import aiohttp


URL = "https://api.scryfall.com"


class Card:
    def __init__(self, uuid: Text, name: Text, image: Text) -> None:
        self.uuid = uuid
        self.name = name
        self.image = image

    @classmethod
    def from_json(self, data: Dict[Text, Any]) -> "Card":
        return Card(data["id"], data["name"], data["image_uris"]["normal"])


class ScryfallAPI:
    def __init__(self) -> None:
        self._http_client = None

    async def _client(self) -> aiohttp.ClientSession:
        if not self._http_client:
            self._http_client = aiohttp.ClientSession(raise_for_status=True)

        return self._http_client

    async def search_cards(
        self,
        card_type: Optional[Text] = None,
        card_subtype: Optional[Text] = None,
        card_creature_type: Optional[Text] = None,
        card_color: Optional[Text] = None,
        card_rarity: Optional[Text] = None,
    ) -> List[Card]:
        q = ""

        params = [
            ("type", card_type),
            ("type", card_subtype),
            ("type", card_creature_type),
            ("color", card_color),
            ("rarity", card_rarity),
        ]

        for param_name, param_val in params:
            if param_val:
                q += f" {param_name}:{param_val}"

        if not q:
            raise ValueError

        params = {"q": q}

        client = await self._client()
        async with client.get(URL + "/cards/search", params=params) as resp:
            ls = await resp.json()
            results = []

            for card in ls["data"]:
                try:
                    results.append(Card.from_json(card))
                except KeyError:
                    pass

            return results

    async def random_card(self) -> Optional[Card]:
        client = await self._client()

        async with client.get(URL + "/cards/random") as resp:
            data = await resp.json()
            try:
                return Card.from_json(data)
            except KeyError:
                return None


api = ScryfallAPI()


class PreSearchCardsAction(Action):
    def name(self) -> Text:
        return "action_pre_search_cards"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ok! Here's the card info I understood:")

        card_type = tracker.get_slot("card_type")
        card_subtype = tracker.get_slot("card_subtype")
        card_creature_type = tracker.get_slot("card_creature_type")
        card_color = tracker.get_slot("card_color")
        card_rarity = tracker.get_slot("card_rarity")

        if card_type:
            dispatcher.utter_message(text=f"The card's type is: {card_type}.")

        if card_subtype:
            dispatcher.utter_message(text=f"The card's subtype is: {card_subtype}.")

        if card_creature_type:
            dispatcher.utter_message(
                text=f"The creature's type is: {card_creature_type}."
            )

        if card_color:
            dispatcher.utter_message(text=f"The card's color is: {card_color}.")

        if card_rarity:
            dispatcher.utter_message(text=f"The card's rarity is: {card_rarity}.")

        dispatcher.utter_message(text="Searching...")


class SearchCardsAction(Action):
    def name(self) -> Text:
        return "action_search_cards"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        card_type = tracker.get_slot("card_type")
        card_subtype = tracker.get_slot("card_subtype")
        card_creature_type = tracker.get_slot("card_creature_type")
        card_color = tracker.get_slot("card_color")
        card_rarity = tracker.get_slot("card_rarity")

        cards = await api.search_cards(
            card_type=card_type,
            card_subtype=card_subtype,
            card_creature_type=card_creature_type,
            card_color=card_color,
            card_rarity=card_rarity,
        )

        for card in cards[:5]:
            dispatcher.utter_message(text=f"Found this card: {card.name}")

        return []


class RandomCardAction(Action):
    def name(self) -> Text:
        return "action_random_card"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        card = None
        while not card:
            card = await api.random_card()

        dispatcher.utter_message(text="Here's a random card:")
        dispatcher.utter_message(text=f"{card.name}")
