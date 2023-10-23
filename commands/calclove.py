import discord
import asyncio
import random

async def calcLove(client, message):
    ranNum = random.randint(0, 100)
    person1 = message.content.split(' ')[1]
    person2 = message.content.split(' ')[2]
    if ranNum < 25:
        finalMsg = f"The % of love between {person1} and {person2} is: {ranNum}%... You guys shouldn´t be together"
    elif ranNum < 50 and ranNum > 25:
        finalMsg = f"The % of love between {person1} and {person2} is: {ranNum}%... Bfff not bad keep grinding ;)"
    elif ranNum < 75 and ranNum > 50:
        finalMsg = f"The % of love between {person1} and {person2} is: {ranNum}%... Eyoo you guys really love each other, good job ;)"
    elif ranNum <= 100 and ranNum > 75:
        finalMsg = f"The % of love between {person1} and {person2} is: {ranNum}%... wtfff just get married XDD :thumbsup: :love_hotel: "

    await message.channel.send(finalMsg)