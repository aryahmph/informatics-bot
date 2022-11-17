from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionBidangKonsentrasiDescription(Action):
    dict = {
        "sistem cerdas": "Sistem cerdas (intelligent system) adalah sistem yang dibangun dengan menggunakan teknik-teknik artificial intelligence (kecerdasan buatan).",
        "sistem terdistribusi": "Sistem terdistribusi adalah kumpulan komputer otonom yang dihubungkan oleh jaringan dengan software yang dirancang untuk menghasilkan fasilitas komputerisasi terintegrasi dianggap oleh pengguna sebagai satu sistem komputer tunggal.",
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


class ActionAskAngkatan(Action):
    def name(self) -> Text:
        return "action_ask_angkatan"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        angkatan = int(tracker.get_slot("angkatan"))
        if angkatan and 2017 <= angkatan <= 2022:
            if 2017 <= angkatan <= 2020:
                dispatcher.utter_message(
                    text=f"Baik, kamu termasuk kurikulum 2017, mata kuliah apa yang ingin ditanyakan?"
                )
            else:
                dispatcher.utter_message(
                    text=f"Baik, kamu termasuk kurikulum 2021, mata kuliah apa yang ingin ditanyakan?"
                )
        else:
            dispatcher.utter_message(
                text="Angkatan tidak valid"
            )
        return []
