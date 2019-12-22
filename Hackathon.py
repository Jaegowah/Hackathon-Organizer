# author: Grigorii Gerdzhikov
import datetime as dt
import random as rd
import json as json
from Player import *


class Hackathon:
    def __init__(self, player_count: int, player_names):
        self.hackathon_id = "hackathon__" + str(dt.datetime.utcnow().strftime("%Y-%m-%d_%H:%M:%S")) + "__" + str(rd.randint(0, 100))
        self.players_list = {}
        for i in range(0, player_count):
            self.players_list.update({player_names[i]: Player(self.hackathon_id, i, player_names[i])})