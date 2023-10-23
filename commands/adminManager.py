import discord
import sqlite3
import asyncio

async def addAdmin(client, message, listAdmin, cursor, conn):
    newAdmin = message.content.split(' ')[1]
    if newAdmin not in listAdmin:
        listAdmin.append(newAdmin)
        await message.channel.send(f'New admin added, Welcome {newAdmin}')

        # Guardar en la base de datos
        cursor.execute("INSERT INTO admins (nombre, es_admin) VALUES (?, ?)", (newAdmin, True))
        conn.commit()
    else:
        await message.channel.send(f'{newAdmin} is already an admin.')

async def removeAdmin(client, message, listAdmin, cursor, conn):
    targetAdmin = message.content.split(' ')[1]
    if targetAdmin != 'magno1337':
        if targetAdmin in listAdmin:
            listAdmin.remove(targetAdmin)
            await message.channel.send(f'{targetAdmin} removed from admins.')

            # Eliminar de la base de datos
            cursor.execute("DELETE FROM admins WHERE nombre = ?", (targetAdmin,))
            conn.commit()
        else:
            await message.channel.send(f'{targetAdmin} is not an admin.')
    else:
        await message.channel.send('You cant delete Mango´s Admin rights, he´s my father ;)')