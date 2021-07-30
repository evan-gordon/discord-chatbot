import calendar as c, random
import mastermind
from discord.ext import commands
from datetime import date

COMMAND_PREFIX = '>'

class Chad(commands.Bot):
  """

  help command implicitly created
  """

  def __init__(self, token):
    if token == "" or token is None:
      raise Exception('Failed to find client token')

    self.token = token
    super().__init__(command_prefix=COMMAND_PREFIX)
    cmds = [
        self.ask,
        self.echo,
        self.calendar
    ]
    for cmd in cmds:
      self.add_command(cmd)

    self.brain = mastermind.Brain()
    self.brain.set_entity_function("toss_coin", self.toss_coin)

  def run(self):
    super().run(self.token, reconnect=True)

  async def on_ready(self):
    print(f'{self.user} has logged in!')

  async def on_message(self, message):
    print(message.content)
    print(message)

    # the bot should not respond to itself
    if message.author == self.user:
      return

    if message.content.startswith('>'):
      await self.process_commands(message)
    elif (message.content.startswith(f'<@!{self.user.id}>') or
          message.content.startswith(f'<@{self.user.id}>')):

      updated_msg = message.content.replace(f'<@!{self.user.id}>', '')
      print(updated_msg)
      reply = self.brain.respond(updated_msg)
      if not reply:
        reply = "Sorry, I didn't quite get that :(" 

      print(f'Replying with: {reply}, To: {message.author}')
      # print(bot.commands())
      await message.channel.send(reply)

  @commands.command()
  async def ask(ctx, *, arg_text):
    ctx.send("42")

  # currently this will error out if no text was provided after the command
  # need to return a response on error
  @commands.command()
  async def echo(ctx, *, arg_text):
    """Displays the text that was sent to the bot"""
    await ctx.send(arg_text)

  @commands.command()
  async def calendar(ctx, *, arg_text):
    """
    Displays a human readable view of this month's calendar.

    Need to later highlight dates with appointments on them.
    Need the ability to add an event to the calender and persist it.
    Need to be able to have reoccuring events.
    """
    split_args = arg_text.split(" ")
    sub_command = split_args[0]
    if sub_command == "show":
      today = date.today()
      cal = c.TextCalendar()
      await ctx.send(f"```{cal.formatmonth(today.year, today.month)}```")
    elif sub_command == "add":
      await ctx.send("added new event")
    else:
      await ctx.send(f"No command with arg: {arg_text}, found." +
                     " Try `>help` to see more about this command"
      )

  def toss_coin(*args, results):
    coin_sides = ["heads", "tails"]
    random.shuffle(coin_sides)
    results["coin_side"] = random.choice(coin_sides)
