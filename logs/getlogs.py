import discord
import asyncio
import os
import sys

global listNombres
global idListNombres


listNombres = [

    'idOs',
    'announceLog',
    'imageEmbedLog',
    'pingLog',
    'timerLog',
    'addAdminLog',
    'removeAdminLog',
    'listAdminsLog',
    'deleteLog',
    'dbLog',
    'calcLoveLog',
    'timestampLog'
    
]

idListNombres = [

    1165661890366672976,
    1165662471575588914,
    1165662518765686784,
    1165662547119186031,
    1165662575212646541,
    1165662600072286331,
    1165662623547805796,
    1165662657295159306,
    1165662671828439090,
    1165683336904196206,
    1165707877911105546,
    1165735627770306592

]


async def getAction(client, message, action):
    index = listNombres.index(action)
    canal_id = idListNombres[index]
    canal = client.get_channel(canal_id)

    if canal:
        # Crear un mensaje enriquecido (Rich Embed)
        embed = discord.Embed(title="Acción Realizada",
                              description="Un usuario ha realizado una acción", color=0xff0000)

        # Añadir los campos
        embed.add_field(name="Autor", value=str(message.author), inline=False)
        embed.add_field(name="Mensaje", value=str(message.content), inline=False)

        # Enviar el mensaje enriquecido
        await canal.send(embed=embed)

    if canal_id == 'deleteLog':
        await canal.send(f'')
