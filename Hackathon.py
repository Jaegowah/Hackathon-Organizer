# author: Grigorii Gerdzhikov
import datetime as dt
import random as rd
import json as json
from Player import *


class Hackathon:
    def __init__(self):
        self.hackathon_id = "hackathon__" + str(dt.datetime.utcnow().strftime("%Y-%m-%d_%H:%M:%S")) + "__" + str(rd.randint(0, 100))
        self.players = {}

    def load_players_from_list(self, list_of_players):
        for index, player_name in enumerate(list_of_players):
            self.players.update({player_name: Player(self.hackathon_id, index, player_name)})

    def output_as_dict(self) -> dict:
        players_list_extended = {}
        for key, player_object in self.players.items():
            players_list_extended.update({key: player_object.output_as_dict()})

        full_object_dict = {
            "hackathon_id": self.hackathon_id,
            "player_count": len(self.players),
            "players": players_list_extended
        }

        return full_object_dict

    def output_as_json(self) -> str:
        return json.dumps(self.output_as_dict(), indent=5)
