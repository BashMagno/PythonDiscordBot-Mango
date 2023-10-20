
import discord
import asyncio
from presence import update_presence
from embeds import sendEmbed, sendEmbedwImage

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# Cargar nombres de administradores desde el archivo
with open('listaAdmins.txt', 'r') as file:
    listAdmin = file.read().splitlines()

with open('listaSuperAdmins.txt', 'r') as file:
    listSuperAdmin = file.read().splitlines()

with open('token.txt', 'r') as file:
    token = file.read()


@client.event
async def on_ready():
    print(f'Bot iniciado como {client.user.name}')
    await update_presence(client)

@client.event
async def on_message(message):

    # Comprobar que el que envia el mensaje no es el bot
    if message.author == client.user:
        return

    if message.content.startswith('$announce'):
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

    if message.content.startswith('$imageEmbed'):
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


    if message.content == '$ping':
        await message.channel.send('Pong!')

    if message.content.startswith('$timer'):
        tiempo = int(message.content.split(' ')[1])
        unidad = str(message.content.split(' ')[2])

        if unidad == 'minutes':
            await message.channel.send(f'Timer of {tiempo} minute/s started.')
            await asyncio.sleep(tiempo * 60)
            await message.channel.send(f'Time ended! {tiempo} minute/s passed.')
        elif unidad == 'seconds':
            await message.channel.send(f'Timer of {tiempo} second/s started.')
            await asyncio.sleep(tiempo)
            await message.channel.send(f'Time ended! {tiempo} second/s passed.')

    # Requiere verificacion admin | Admin rights required

    if message.content.startswith('$addAdmin'):
        if message.author.name in listAdmin:
            newAdmin = message.content.split(' ')[1]
            if newAdmin not in listAdmin:
                listAdmin.append(newAdmin)
                await message.channel.send(f'New admin added, Welcome {newAdmin}')

                # Guardar en el archivo
                with open('listaAdmins.txt', 'a') as file:
                    file.write(newAdmin + '\n')
            else:
                await message.channel.send(f'{newAdmin} is already an admin.')
        else:
            await message.channel.send('[Error]$-> Sorry you dont have enough permissions to do this.')

    if message.content.startswith('$removeAdmin'):
        if message.author.name in listAdmin:
            targetAdmin = message.content.split(' ')[1]
            if targetAdmin != 'magno1337':
                if targetAdmin in listAdmin:
                    listAdmin.remove(targetAdmin)
                    await message.channel.send(f'{targetAdmin} removed from admins.')

                    # Actualizar el archivo
                    with open('listaAdmins.txt', 'w') as file:
                        for admin in listAdmin:
                            file.write(admin + '\n')
                else:
                    await message.channel.send(f'{targetAdmin} is not an admin.')
            else:
                await message.channel.send('You cant delete Mango´s Admin rights,  he´s my father ;)')
        else:
            await message.channel.send('[Error]$-> Sorry you dont have enough permissions to do this.')


    if message.content.startswith('$delete'):
        if message.author.name in listAdmin:
            fMsg = [int(param) for param in message.content.split(' ')[1:]]

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

    # Requiere privilegio SuperAdmin | SuperAdmin / SuperUser rights required

    if message.content == '$disconnect':
        if message.author.name in listSuperAdmin:
            await message.channel.send('Disconnecting...')
            await client.close()
        else:
            await message.channel.send(f'{message.author.name}, you dont have enough permissions to do this.')

# Iniciar el bot
client.run(token)
