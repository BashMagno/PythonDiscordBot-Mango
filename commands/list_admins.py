import discord
import sqlite3
from logs import getlogs

async def list_admins(client, message, listAdmin, cursor):
    if message.author.name in listAdmin:
        cursor.execute('SELECT nombre FROM admins')
        admins = [row[0] for row in cursor.fetchall()]
        admin_list = '\n'.join(admins)
        embed = discord.Embed(title="Lista of Administrators", description=admin_list, color=0x00ff00)
        await message.channel.send(embed=embed)
        await getlogs.getAction(client, message, 'listAdminsLog')
    else:
        await message.channel.send('No tienes permisos para listar administradores.')
