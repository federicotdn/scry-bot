from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class SearchCardsAction(Action):
    def name(self) -> Text:
        return "action_search_cards"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here's the card info:")

        card_type = tracker.get_slot("card_type") or "no type"
        card_color = tracker.get_slot("card_color") or "no color"
        card_rarity = tracker.get_slot("card_rarity") or "no rarity"

        dispatcher.utter_message(
            text=f"Type: {card_type}, color: {card_color}, rarity: {card_rarity}"
        )

        return []
