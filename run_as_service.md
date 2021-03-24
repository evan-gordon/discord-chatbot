# Booting at startup

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