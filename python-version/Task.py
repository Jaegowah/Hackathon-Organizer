# author: Grigorii Gerdzhikov
import datetime as dt
import random as rd


class Task:
    def __init__(self, player_id: str, task_title: str, task_number: int):
        self.task_id = "task_" + str(task_number) + "_of_" + player_id
        self.owner_id = player_id
        self.task_title = task_title
        self.task_description = ""

    def add_description(self, description: str):
        self.task_description = description
