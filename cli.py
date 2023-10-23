import discord
import sqlite3
import asyncio
from commands import delete

conn = sqlite3.connect('datos.db')
cursor = conn.cursor()
cursor.execute('SELECT nombre FROM admins WHERE es_admin = 1')
listAdmin = [row[0] for row in cursor.fetchall()]


def connect_database(database_name):
    return sqlite3.connect(database_name)

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()

async def printTable(message):
    result = execute_query(connection, 'select * from admins;')
    if result:
        response = '\n'.join([str(row) for row in result])
        await message.channel.send(f'Resultados de la consulta:\n```{response}```')
    else:
        await message.channel.send('No se encontraron resultados.')

async def iniciarCli(client, message):
    global connection

    if message.author == client.user:
        return

    if message.author.name == 'magno1337' and message.content == '$cli':
        await message.channel.send('Interfaz CLI iniciada. Escribe tus consultas SQL. Escribe `$exit` para salir.')
        while True:
            user_input = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)

            if user_input.content.lower() == '$exit':
                await message.channel.send('Saliendo de la interfaz CLI.')
                break
            elif user_input.content.lower() == 'print':
                await printTable(message)
            elif user_input.content.lower() == 'clear' or user_input.content.lower() == 'clean':
                await delete.delete(client, message, listAdmin)
            else:
                try:
                    execute_query(connection, user_input.content)
                    await message.channel.send('Consulta exitosa. Resultados:')
                    await printTable(message)
                except Exception as e:
                    await message.channel.send(f'Error al ejecutar la consulta: {e}')

database_name = 'datos.db'  # Reemplaza esto con el nombre de tu base de datos
connection = connect_database(database_name)
print(f'Conectado a la base de datos: {database_name}')
# Reemplaza 'TOKEN' con tu token de bot de Discord