import os
import discord
import random 
from dotenv import load_dotenv
from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
token = os.getenv('MAESTRO_FORTUNA')
bot = commands.Bot(command_prefix='maestro')


@bot.event
async def on_ready():
    print(f'maestro se ha conectado a Discord!')
    
@bot.command(name='dados', help='Lanzamiento de dados')
async def roll(ctx, numero_dados:int = 1, number_of_sides:int = 20):
    """ 
    Documentación
    """
    dado = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(numero_dados)
    ]
    await ctx.send(', '.join(dado))
    
bot.run(token)
