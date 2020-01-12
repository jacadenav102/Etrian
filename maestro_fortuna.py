import os
import discord
import random 
import re
import numpy as np
from dotenv import load_dotenv
from discord.ext import commands
from dotenv import load_dotenv
from numpy.random import choice


load_dotenv()
token = os.getenv('MAESTRO_FORTUNA')
bot = commands.Bot(command_prefix='m')


@bot.event
async def on_ready():
    print(f'maestro se ha conectado a Discord!')
    
@bot.command(name='dados', help='Lanzamiento de dados')
async def roll(ctx, numero_dados:int = 1, numero_caras:int = 20,bonificador: int = 0):
    """ 
    Documentación
    """
    resultado = bonificador
    dado = [str(choice(np.arange(1,stop = numero_caras+1,step=1))) for _ in range(numero_dados)] 
    dados = ', '.join(dado)
    
    for valores in re.split(',',dados):
        resultado = resultado + int(valores)

    final = str(resultado) + ' <-- '  + dados  + ' + ' + str(bonificador)
    
    
    await ctx.send(final)
    
bot.run(token)
