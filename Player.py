# author: Grigorii Gerdzhikov
import random as rd
from Task import *


class Player:
    def __init__(self, hackathon_id: str, player_number: int, player_name: str):
        self.player_id = "player_" + str(player_number)
        self.player_name = player_name
        self.hackathon_id = hackathon_id
        self.player_tasks = []

    def add_new_task(self, task_name: str):
        self.player_tasks.append(Task(self.player_id, task_name, self.player_tasks.count()+1))
