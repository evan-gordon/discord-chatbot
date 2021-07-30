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

# run
python main.py
```

If you want to run this as a startup service see:

[run_as_service.md](./run_as_service.md)

## Future Plans

* research swapping BERT for snips-nlu <https://nbviewer.jupyter.org/github/m2dsupsdlclass/lectures-labs/blob/master/labs/06_deep_nlp/Transformers_Joint_Intent_Classification_Slot_Filling_rendered.ipynb>
* in train make sure /data/models dir exists

* die roll
* daily news link
* stonk info?
* move from pipenv to poetry

## Discord Bot API Notes

token can be generated at:

<https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro>

Navigate to the `Bot` page, to retrieve or generate a new token.

## Before Commits

remove git credentials from Pipfile and .lock
