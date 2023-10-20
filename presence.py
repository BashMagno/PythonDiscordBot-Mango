import discord
from discord import Game, Activity, ActivityType

async def update_presence(client):
    await client.change_presence(
        activity=Game(name="Mango the goat B)"),  # Puedes cambiar el nombre del juego
        status=discord.Status.online,    # Estado del bot (online, idle, dnd, invisible)
    )
