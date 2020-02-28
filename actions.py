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
        self._client = None

    async def search_cards(
        self,
        card_type: Optional[Text] = None,
        card_color: Optional[Text] = None,
        card_rarity: Optional[Text] = None,
    ) -> List[Card]:
        q = ""

        if card_type:
            q += f"type:{card_type}"

        if card_color:
            q += f" color:{card_color}"

        if card_rarity:
            q += f" rarity:{card_rarity}"

        if not q:
            raise ValueError

        params = {"q": q}

        if not self._client:
            self._client = aiohttp.ClientSession(raise_for_status=True)

        async with self._client.get(URL + "/cards/search", params=params) as resp:
            ls = await resp.json()
            results = []

            for card in ls["data"]:
                try:
                    results.append(Card.from_json(card))
                except KeyError:
                    pass

            return results


class SearchCardsAction(Action):
    def __init__(self) -> None:
        self._api = ScryfallAPI()

    def name(self) -> Text:
        return "action_search_cards"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here's the card info:")

        card_type = tracker.get_slot("card_type")
        card_color = tracker.get_slot("card_color")
        card_rarity = tracker.get_slot("card_rarity")

        dispatcher.utter_message(
            text=f"Type: {card_type}, color: {card_color}, rarity: {card_rarity}"
        )

        dispatcher.utter_message(text="Searching...")

        cards = await self._api.search_cards(
            card_type=card_type, card_color=card_color, card_rarity=card_rarity
        )

        for card in cards[:5]:
            dispatcher.utter_message(text=f"Found this card: {card.name}")

        return []
