from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBidangKonsentrasiDescription(Action):
    def name(self) -> Text:
        return "action_bidang_konsentrasi_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bidang_konsentrasi = tracker.get_slot("bidang_konsentrasi")
        if not bidang_konsentrasi:
            dispatcher.utter_message(
                template="utter_description_bidang_konsentrasi",
                text="Maaf, bidang konsentrasi tersebut tidak terdata pada sistem kami"
            )
        else:
            dispatcher.utter_message(
                template="utter_description_bidang_konsentrasi",
                text=f"pilihan mu: {bidang_konsentrasi}!"
            )
        return []
