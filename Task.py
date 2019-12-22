# author: Grigorii Gerdzhikov
import datetime as dt
import random as rd


class Task:
    def __init__(self, player_id: str, task_name: str, task_number: int):
        self.task_id = "task_" + str(task_number) + "_of_" + player_id
        self.owner_id = player_id
        self.task_name = task_name
