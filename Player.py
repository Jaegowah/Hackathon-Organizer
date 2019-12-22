# author: Grigorii Gerdzhikov
import random as rd
from Task import *


class Player:
    def __init__(self, hackathon_id: str, player_number: int, player_name: str):
        self.player_id = "player_" + str(player_number)
        self.player_name = player_name
        self.hackathon_id = hackathon_id
        self.tasks = {}

    def add_new_task(self, task_name: str):
        self.tasks.update({task_name: Task(self.player_id, task_name, len(self.tasks))})

    def output_as_dict(self) -> dict:
        tasks_dict = {}
        for key, task_object in self.tasks.items():
            tasks_dict.update({key: task_object.__dict__})

        output = {
            "player_id": self.player_id,
            "name": self.player_name,
            "participates_in": self.hackathon_id,
            "tasks": tasks_dict
        }

        return output
