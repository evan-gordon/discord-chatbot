# API For Bot Connection

## Features

Currently supports

```bash
>ask <question>
#responds with 42

@<botname> <text>
#responds with 'hi'
```

## Setup

create these env variables in your system if you intend to try manually running

```bash
export OWM_API_KEY=<weather_key>
export DISCORD_BOT_KEY=<discord_key>
```

```bash
# download language presets
python -m snips_nlu download en

# setup the bot framework and bot
python train.py
```

### Booting at startup

replace all `<>` tags in `discordbot.service` as well as `startup.sh`

```bash
# run from project directory
# add service file to systemd services
cp discordbot.service /lib/systemd/system/

# enabling / running service commands
systemctl start discordbot
systemctl stop discordbot
systemctl enable discordbot

# checkinglogs
systemctl status -n10 discordbot
journalctl -u discordbot.service -b
```

Note:
the service file tells systemd to call this projects `startup.sh` file. both files must be configured correctly for this to work

## Future Plans

* research swapping BERT for snips-nlu <https://nbviewer.jupyter.org/github/m2dsupsdlclass/lectures-labs/blob/master/labs/06_deep_nlp/Transformers_Joint_Intent_Classification_Slot_Filling_rendered.ipynb>
* in train make sure /data/models dir exists

## Discord bot notes

token can be generated at:

<https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro>

## Before Commits

remove git credentials from Pipfile and .lock