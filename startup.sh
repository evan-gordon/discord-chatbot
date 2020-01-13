#! /bin/sh

# Note: you may need to run `sudo chmod 755 startup.sh` to fix permission errors

CURR_USER=$(whoami)
LOG_FILE='/tmp/discordbot.log'

# these lines can be safely deleted
echo "Starting discordbot service as $CURR_USER"
echo "bot key: $DISCORD_BOT_KEY"

<path_to_pipenv>/pipenv run -v python <path_to_project>/discord-chatbot/discord_bot_client.py > $LOG_FILE

echo "python output logged at: $LOG_FILE"

exit 0
