from  ThickBot import Bot
from discord.ext import commands



if __name__ == '__main__':
    path = "database/sentences.txt"
    jeton =""  # token
    prefix = 'dridri'


    bot = commands.Bot(command_prefix=f'{prefix} ')
    bot.add_cog(Bot(bot,path))
    bot.run(jeton)
    print("See you next time")
