import discord
import TOKEN

#channels here
starboard = 1509464988983754932
bot = 1508097475419050014
starboard2 = 1511635867146653736

intents = discord.Intents.default()
intmescon = intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == starboard2:
        return
    if message.channel.id == bot:
        messagecontent = message.content.lower()
        if messagecontent == "hello":
            await message.channel.send("Hello!")
        if messagecontent == "froyo, what do you think of miri and gab?":
            await message.channel.send("goated")
        if messagecontent == ("what can froyo do?"):
            await message.channel.send("I can give you a role, and rate your work!")
        if messagecontent == "charlie kirk":
            await message.channel.send("counting and not counting gang violence")
    if message.channel.id == starboard:
        if 1 > 0:
            await message.add_reaction("⭐")

    
    


client.run(TOKEN.TOKEN)
