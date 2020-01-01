import discord, mastermind, os
from discord.ext.commands import Bot
from functools import reduce

bot = Bot(command_prefix='>')
brain = mastermind.Brain()

@bot.event
async def on_ready():
  print(f'{bot.user} has logged in!')

# help command implicitly created

@bot.command()
async def ask(ctx):
  """Answers all your questions"""
  answer = 42
  print(f'Answering: {answer}')
  await ctx.send(answer)

@bot.event
async def on_message(message):
  print(message.content)
  print(message)
  if message.author == bot.user:
    return
  elif message.content.startswith('>'):
    await bot.process_commands(message)
  elif message.content.startswith(f'<@!{bot.user.id}>'):
    updated_msg = message.content.replace(f'<@!{bot.user.id}>', '')
    print(updated_msg)
    reply = brain.respond(updated_msg)
    if not reply:
      reply = "Sorry, I didn't quite get that :(" 

    print(f'Replying with: {reply}, To: {message.author}')
    # print(bot.commands())
    await message.channel.send(reply)

discord_key = os.environ.get('DISCORD_BOT_KEY')
bot.run(discord_key)