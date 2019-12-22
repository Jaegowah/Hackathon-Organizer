from Hackathon import *

players_list = ["max", "marie", "mario"]

# create hackathon
my_hackathon = Hackathon()
my_hackathon.load_players_from_list(players_list)

my_hackathon.players["max"].add_new_task("Invitations")
my_hackathon.players["max"].tasks["Invitations"].add_description("send invitations to all team members")

print(my_hackathon.output_as_json())
