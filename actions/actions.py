from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionBidangKonsentrasiDescription(Action):
    dict = {
        "sistem cerdas": "Sistem cerdas (intelligent system) adalah sistem yang dibangun dengan menggunakan teknik-teknik artificial intelligence (kecerdasan buatan).",
        "sistem terdistribusi": "Sistem terdistribusi adalah kumpulan komputer otonom yang dihubungkan oleh jaringan dengan software yang dirancang untuk menghasilkan fasilitas komputerisasi terintegrasi dianggap oleh pengguna sebagai satu sistem komputer tunggal.",
        "grafis dan visual": "yang ini grafis dan visual"
    }

    def name(self) -> Text:
        return "action_bidang_konsentrasi_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bidang_konsentrasi = tracker.get_slot("bidang_konsentrasi").lower()
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
        kurikulum = 2017
        if angkatan and 2017 <= angkatan <= 2022:
            if 2017 <= angkatan <= 2020:
                dispatcher.utter_message(
                    text=f"Baik, kamu termasuk kurikulum 2017, mata kuliah apa yang ingin ditanyakan?"
                )
            else:
                kurikulum = 2021
                dispatcher.utter_message(
                    text=f"Baik, kamu termasuk kurikulum 2021, mata kuliah apa yang ingin ditanyakan?"
                )
            return [SlotSet("kurikulum", kurikulum)]
        else:
            dispatcher.utter_message(
                text="Angkatan tidak valid"
            )
        return []


class ActionAskMataKuliahDescription(Action):
    dict = {
        2017: {
            "algoritma dan pemograman 1": "Algoritma dan Pemograman I merupakan mata kuliah yang mempelajari tentang konsep-konsep dasar pada pemograman, seperti algoritma, input/output, tipe data, variabel, pengkondisian, perulangan, dan array. Bahasa pemograman yang biasanya digunakan pada mata kuliah ini adalah Java.\n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan tidak memiliki prasyarat mata kuliah lain untuk mengambilnya.",
            "algoritma dan pemograman 2": "Algoritma dan Pemograman II merupakan mata kuliah yang mempelajari algoritma lanjutan seperti pengurutan, pencarian, array 2 dimensi, dan error handling.\n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan memiliki prasyarat mata kuliah Algoritma dan Pemograman 1 untuk mengambilnya.",
            "pemograman web 1": "Pemograman Web I merupakan mata kuliah yang mempelajari tentang dasar-dasar dari web, khusunya pada bagian front-end yaitu HTML, CSS, dan Javascript. \n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan memiliki prasyarat mata kuliah Algoritma dan Pemograman 1 untuk mengambilnya.",
            "struktur data": "Struktur Data merupakan mata kuliah yang mempelajari tentang macam-macam struktur data yang ada menggunakan bahasa Java, seperti Stack, Queue, LinkedList, ArrayList, dan Binary Tree.\n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan memiliki prasyarat mata kuliah Algoritma dan Pemograman 2 untuk mengambilnya."
        },
        2021: {
            "pemrograman komputer": "pemrograman komputer merupakan mata kuliah yang mempelajari tentang dasar-dasar pemrograman komputer. Materi yang diberikan dalam mata kuliah ini antara lain adalah pengantar pemrograman komputer yang meliputi tujuan pemrograman, pemrograman dalam konteks aplikasi, perspektif programmer, dan lingkungan pemrograman\n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan tidak memiliki prasyarat mata kuliah lain untuk mengambilnya.",
            "pengantar teknologi informasi": "pengantar teknologi informasi merupakan mata kuliah yang mempelajari teknologi komputer dan teknologi telekomunikasi. Materi mata kuliah ini antara lain meliputi konsep, komponen, klasifikasi dan peranan teknologi informasi. Mata kuliah ini bertujuan agar mahasiswa dapat memahami perkembangan ilmu komputer, dasardasar perangkat keras, perangkat lunak dan mengenal peranan teknologi informasi dari berbagai bidang keilmuan.\n\nMata kuliah ini memiliki bobot yaitu 3 SKS dan tidak memiliki prasyarat mata kuliah lain untuk mengambilnya.",
            "pengantar algoritma dan struktur data": "pengantar algoritma dan struktur data merupakan mata kuliah yang mempelajari konsep, prinsif, dan mekanisme untuk menyusun prosedur sistematis dalam memecahkan permasalahan menggunakan langkahlangkah yang terbatas yang dinyataka dengan bahasa alami, flowchart, dan/atau pseudocode. \n\n Mata kuliah ini memiliki bobot yaitu 3 SKS dan tidak memiliki prasyarat mata kuliah lain untuk mengambilnya.",
            "organisasi dan arsitektur komputer": "organisasi dan arsitektur komputer merupakan mata kuliah yang mempelajari tentang sejarah perkembangan teknologi komputer, apa yang dimaksud dengan komputer dan bagaimana komputer dapat membantu pekerjaan manusia.\n\n Mata kuliah ini memiliki bobot yaitu 3 SKS dan tidak memiliki prasyarat mata kuliah lain untuk mengambilnya."
        }
    }

    def name(self) -> Text:
        return "action_ask_mata_kuliah_description"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        kurikulum = tracker.get_slot("kurikulum")
        if not kurikulum:
            dispatcher.utter_message(
                text="Kurikulum belum dimasukkan!\nAngkatan berapa anda?"
            )
        elif int(kurikulum) not in self.dict:
            dispatcher.utter_message(
                text="Kurikulum tidak valid"
            )

        kurikulum = int(kurikulum)
        mata_kuliah = tracker.get_slot("mata_kuliah")
        if mata_kuliah and mata_kuliah.lower() in self.dict[kurikulum]:
            dispatcher.utter_message(
                text=f"{self.dict[kurikulum][mata_kuliah]}"
            )
        else:
            dispatcher.utter_message(
                text="Mata kuliah yang anda masukkan tidak valid"
            )
        return []
