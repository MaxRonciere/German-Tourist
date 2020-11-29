from  ThickBot import Bot
from discord.ext import commands

reponse_rage = [
    "ptin je t'ai rien dit depuis longtemps ques-tu me veut la ? la merde",
    "De toute façon tu as toujours raison et jamais tord",
    "Vas y je te laisse penser que la terre est plate",
    "Mais qu'est ce que tu me racompte"
    ]


if __name__ == '__main__':
    jeton ="YOUR TOKEN"
    bot = commands.Bot(command_prefix='cooking ')
    bot.add_cog(Bot(bot,reponse_rage))
    bot.run(jeton)
    print("See you next time")
