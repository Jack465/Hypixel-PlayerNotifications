# Hypixel Player Notifications
This script queries the Hypixel (MC Server) API every 30 seconds to see if a player is online (or if they have disconnected). If it detects a change in the players connection status (eg the player logs in, or the player logs out), a web request is made to a Discord webhook, which puts a message in the Discord Chat saying "Player (PlayerName) is (offline/online)

# Requirements
Python 3 - `sudo apt install python3 python3-pip`
```
pip3 install requests
```

# How to use.

## Hypixel
Firstly you need to obtain your Hypixel API key by logging into the server, and issuing the chat command "/api new" (if you already have an API key, you can skip this step). The output of that command will look like this 

![APIKEY](https://i.imgur.com/0QcmGvs.jpg)

After getting the Hypixel API key from in-game you will paste it between the quotes on Line 7 of the script.

## Discord 
Next you will need to setup the webhook for Discord.

* First you will navigate to the channel where you want the messages sent to, and then hover over the channel name and click the settings icon

![Discord1](https://i.imgur.com/vLAnu2A.png)

* After that you will press "Integrations" on the menu that shows up, and then click "Webhook", and then click "New Web Hook"

![Discord2](https://i.imgur.com/1WUx5bm.png)

* When you click "New Webhook" you will be prompted to enter a name for the Web Hook, and the channel that you want the messages to be posted in. Select the appropriate options for your server setup. After you have set a name, and channel click the "Copy Webhook URL" Button and then insert the copied link between the quotes on Line 8. 

## Final Setup

We are nearing the end of setup now, all you have to do to complete is the following:
* Insert your username on Line 6 - the script will automatically convert this to a UUID so you don't have to worry about that. 
* Run the script using `python3 main.py`
* You may want to run the script in Screen so you can exit the ssh session without the program exiting to do that you will run the following commands
    * ``` sudo apt install screen ```
    * ``` screen -dm bash -c 'python3 /path/to/your/script.py'```

## Tip
If you are feeling generous, and appreciate the work done, feel free to tip to the following Crypto addresses:
<sup>please don't feel like you're obligated to tip, everything is offered free of charge.</sup>
* BTC - 16bBvNAYDTQ4PLhGXU4gdr6Evr1iADfZpw
* XMR - 49t4ZvemSkyfWiK65LCYVo3v2uE19BPJf2hp4K8U8TbqUbzYVjxtkBFV7E9THYJXE9TPfQUYBUFgMZ7veHipVzjF12KqBGC
* ETH- 0x4e1ed7f4278b0a607b515a41b42d89fa8f230b17