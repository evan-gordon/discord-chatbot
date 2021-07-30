import os, sys
from discord_bot_client import Chad

if __name__ == "__main__":
  print("Starting bot...")
  try:
      token = os.environ.get('DISCORD_BOT_KEY')

      bot = Chad(token)
      bot.run()
  except Exception:
      e = sys.exc_info()
      print(str(e))
  print("Shutting down...")
