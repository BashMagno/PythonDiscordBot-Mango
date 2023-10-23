import discord
import asyncio
from embeds import sendEmbed, sendEmbedwImage

async def announce(client, message):

    idChannel = message.channel.id
    parts = message.content.split('"')

    # Verificar que haya al menos tres partes (comando, título, descripción)
    if len(parts) >= 4:

        title = parts[1]

        description = parts[3]

        await sendEmbed(client, idChannel, title, description)
    else:
        # Si no hay suficientes partes, notificar al usuario
        await message.channel.send('Usage of the command\n[!announce "<title>" "<description>"].')

async def announceImg(client, message):

    idChannel = message.channel.id
    parts = message.content.split('"')
        
    # Verificar que haya al menos cuatro partes (comando, título, descripción, url de imagen)
    if len(parts) >= 6:
        title = parts[1]
        description = parts[3]
        imgUrl = parts[5]
        
        await sendEmbedwImage(client, idChannel, title, description, imgUrl)
    else:
        # Si no hay suficientes partes, notificar al usuario
        await message.channel.send('Usage of the command\n[!announce "<title>" "<description>" "<imgUrl>"].')