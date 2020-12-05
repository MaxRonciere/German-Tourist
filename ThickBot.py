import discord
from discord.ext import commands
import sys
import csv
from ThickBrain import Brain

def print(object, end='\n'):
    sys.stdout.write(f'{object}{end}')
    sys.stdout.flush()

class Bot(commands.Cog):
    """docstring for Thickbot.
        Thickbot is here , Mad, fat,
        he wants to fight in Uganda
        be he cant. So he gonna troll
        on The internet like in South Park
            - Commando

    """

    def __init__(self, bot,path):
        self.brain = Brain(path)
        self.bot = bot
        self.run = False
        self.name = False


    @commands.command()
    async def on(self,ctx):
        self.run = True
        await ctx.send("We found German tourits")

    @commands.command()
    async def off(self,ctx):
        self.run = False
        await ctx.send("we're cooking them")

  

    @commands.command()
    async def setName(self,ctx, user: discord.User):
        with open('database/name.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=':',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(user.id)])
                print(f'set {user} as the victim id')
                await ctx.send("Save me the head. Like Predator")


    @commands.Cog.listener()
    async def on_ready(self):
        print('[*] Bot opérationnel !')

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.run is True:
            with open('database/name.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in reader:
                    if [str(message.author.id)] == row:
                        channel = message.channel
                        a = self.brain.think()[0][0]
                        await channel.send(f'<@{message.author.id}> {a}')
