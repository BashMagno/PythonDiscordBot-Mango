import discord
import sqlite3
from logs import getlogs 

async def delete(client, message, listAdmin):
    if message.author.name in listAdmin:
        fMsg = [
            int(param) 
            for param in message.content.split(' ')[1:]
        ]

        # Obtener todos los mensajes en el canal
        messages = []
        async for msg in message.channel.history(limit=99):
            if msg.id not in fMsg:
                messages.append(msg)
                print(msg.author, msg.content)

        # Borrar los mensajes
        await message.channel.delete_messages(messages)
    else:
        await message.channel.send('[Error]$-> Sorry you dont have enough permissions to do this.')