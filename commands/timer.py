import discord
import asyncio

async def timer(client, message):
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