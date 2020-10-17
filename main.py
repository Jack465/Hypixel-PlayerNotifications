import requests
import time
import json

#variables to change.
username = "Jack16"
HYPIXEL_API_KEY = "#####" # get from in game using /api new
URL = "######" # setup in the settings of the guild, more in readme.md
# Don't change below this line. 

previous_state = ""

def usernametoUUID(username):
	mcAPI = requests.get("https://api.mojang.com/users/profiles/minecraft/{}".format(username)).json()
	return(mcAPI['id'])

uuid = usernametoUUID(username)

def notify(message):
	data = {}
	data["content"] = message
	data['username'] = "Hypixel Player Status"

	output = requests.post(URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
	try:
		output.raise_for_status()
	except requests.exceptions.HTTPError as err:
		print(err)
	else:
		print("Discord notified that player {} is {}".format(username, previous_state))

try:
	while True:
		data = requests.get("https://api.hypixel.net/player?key={}&uuid={}".format(HYPIXEL_API_KEY, uuid)).json()

		if(data['player']['lastLogin'] < data['player']['lastLogout']):
			if previous_state != "offline":
				previous_state = "offline"
				notify("Player {} is offline".format(username))
		else:
			if previous_state != "online":
				previous_state = "online"
				notify("Player {} is online".format(username))
		time.sleep(30)
except KeyboardInterrupt:
	print("\n\nStopping from keyboard interrupt!")