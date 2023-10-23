
import asyncio
from presence import update_presence
from embeds import sendEmbed, sendEmbedwImage
import sqlite3
import discord
from commands import list_admins, delete, calclove, announce, timer, adminManager  # Añade la importación
from logs import getlogs
import cli

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = '$'

@client.event
async def on_ready():
    print(f'Bot iniciado como {client.user.name}')
    await update_presence(client)

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        es_admin BOOLEAN
    )
''')
conn.commit()

# Verificar si el usuario magno1337 ya existe
cursor.execute("SELECT * FROM admins WHERE nombre=?", ('magno1337',))
resultado = cursor.fetchone()

if not resultado:
    # El usuario no existe, entonces lo insertamos como administrador
    cursor.execute("INSERT INTO admins (nombre, es_admin) VALUES (?, ?)", ('magno1337', 1))
    conn.commit()
else:
    print("El usuario magno1337 ya existe como administrador.")

# Cargar nombres de administradores desde la base de datos
cursor.execute('SELECT nombre FROM admins WHERE es_admin = 1')
listAdmin = [row[0] for row in cursor.fetchall()]

# Read token
with open('token.txt', 'r') as file:
    token = file.read()

@client.event
async def on_message(message):

    # Comprobar que el que envia el mensaje no es el bot
    if message.author == client.user:
        return

    # ANNOUNCE W/O IMAGE COMMAND
    if message.content.startswith(prefix):
        # Obtener el comando y los argumentos
        args = message.content[len(prefix):].split()
        command = args[0]
        args = args[1:]

        if command == 'announce':
            await getlogs.getAction(client, message, 'announceLog')
            await announce.announce(client, message)

        # ANNOUNCE WITH IMAGE COMMAND

        if command == 'imageEmbed':
            await getlogs.getAction(client, message, 'imageEmbedLog')
            await announce.announceImg(client, message)

        # PING COMMAND

        if command == 'ping':
            latency = round(client.latency * 1000, 2)

            await getlogs.getAction(client, message, 'pingLog')
            await message.channel.send(f"```diff\n- Pong! Latency of the server: {latency}ms```")

        # TIMER COMMAND

        if command == 'timer':
            await getlogs.getAction(client, message, 'timerLog')
            await timer.timer(client, message)

        # ADD ADMIN COMMAND

        if command == 'addAdmin':
            await getlogs.getAction(client, message, 'addAdminLog')
            if message.author.name in listAdmin:
                await adminManager.addAdmin(client, message, listAdmin, cursor, conn)
            else:
                await message.channel.send('[Error]$-> Sorry you dont have enough permissions to do this.')

        # REMOVE ADMIN COMMAND

        if command == 'removeAdmin':
            await getlogs.getAction(client, message, 'removeAdminLog')
            if message.author.name in listAdmin:
                await adminManager.removeAdmin(client, message, listAdmin, cursor, conn)
            else:
                await message.channel.send('[Error]$-> Sorry you dont have enough permissions to do this.')

        # ADD ADMIN COMMAND

        if message.author.name == 'magno1337' and command == 'cli':
            await getlogs.getAction(client, message, 'dbLog')
            await cli.iniciarCli(client, message)

        # CALC LOVE COMMAND

        if command == 'calcLove':
            await getlogs.getAction(client, message, 'calcLoveLog')
            await calclove.calcLove(client, message)

        # LIST ADMIN COMMAND

        if command == 'listAdmins':
            await list_admins.list_admins(client, message, listAdmin, cursor)
            await getlogs.getAction(client, message, 'listAdminsLog')

        # DELETE COMMAND

        if command == 'delete':
            await delete.delete(client, message, listAdmin)
            await getlogs.getAction(client, message, 'deleteLog')
client.run(token)
