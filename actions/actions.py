from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBidangKonsentrasiDescription(Action):
    dict = {
        "sistem cerdas": "ini sistem cerdas ges",
        "sistem terdistribusi": "kalo ini sistem terdistribusi",
        "grafis dan visual": "yang ini grafis dan visual"
    }

    def name(self) -> Text:
        return "action_bidang_konsentrasi_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bidang_konsentrasi = tracker.get_slot("bidang_konsentrasi")
        if bidang_konsentrasi and bidang_konsentrasi.lower() in self.dict:
            dispatcher.utter_message(
                text=f"{self.dict[bidang_konsentrasi]}!"
            )
        else:
            dispatcher.utter_message(
                text="Bidang konsentrasi yang anda masukkan tidak valid"
            )
        return []
