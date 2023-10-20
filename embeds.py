import discord

async def sendEmbed(client, id, title, description):

    # Crear un objeto Embed
    embed = discord.Embed(
        title= title,
        description= description,
        color=discord.Color.green()
    )

    # Agregar una imagen a la descripción

    # Enviar el mensaje con el Embed
    channel = client.get_channel(id)  # Reemplaza con el ID del canal
    await channel.send(embed=embed)

async def sendEmbedwImage(client, id, title, description, imageUrl):

    # Crear un objeto Embed
    embed = discord.Embed(
        title= title,
        description= description,
        color=discord.Color.green()
    )

    # Agregar una imagen a la descripción
    embed.set_image(url=imageUrl)  # Reemplaza con la URL de tu imagen

    # Enviar el mensaje con el Embed
    channel = client.get_channel(id)  # Reemplaza con el ID del canal
    await channel.send(embed=embed)


