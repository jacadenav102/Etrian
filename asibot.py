import os
import discord
import re
import random as rd
from dotenv import load_dotenv
from funciones import crea_respusta_patrones
from respuestas import lista_respuestas
from respuestas import lista_negra
from discord.ext import commands



load_dotenv()
token = os.getenv('ASIBOT')
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('asibot se conectó a Discord')


@bot.event
async def on_member_remove(member):
    print(f'{member.name} dejó el servidor')


@bot.event
async def on_message(message):
    print(message.author)
    if (str(message.channel) == 'consulta-con-issac-asibot' or str(message.channel) == f'Direct Message with {message.author}') and str(message.author) !=  'Asibot#1675':
                if crea_respusta_patrones(lista_respuestas,message.content) != None:
                    await message.channel.send(crea_respusta_patrones(lista_respuestas,message.content))
                else:
                    await message.channel.send(lista_respuestas['confusion'])

    else:
        
        if message.content in lista_negra:
            await message.author.create_dm()
            await message.author.dm_channel.send(
            'Ese lenguaje no esta permitido'
        )
        

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hola {member.name}, Bienvenido a mi servidor!'
    )


bot.run(token)