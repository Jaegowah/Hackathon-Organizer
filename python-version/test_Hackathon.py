import datetime as dt
import view_Dashboard as view_Dashboard
from Hackathon import *

players_list = ["GG", "TR", "ES", "DG"]

# create hackathon
my_hackathon = Hackathon(dt.date(2020, 1, 6), dt.datetime(2020, 1, 6, 13), dt.datetime(2020, 1, 6, 15, 30))
my_hackathon.load_players_from_list(players_list)

my_hackathon.players["GG"].add_new_task("Set Up Hackathon")
my_hackathon.players["GG"].tasks["Set Up Hackathon"].add_description("Start Hackathon Tool and explain it.")

# print(my_hackathon.output_as_json())

view_Dashboard.launch_hackathon_dashboard(my_hackathon)