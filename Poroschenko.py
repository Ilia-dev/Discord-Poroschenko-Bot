import discord

slawa = ['Украине!','Мерлоу!']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as',self.user)
    async def on_message(self,message):
        if message.content == 'Слава!':
            await message.channel.send(random.choice(slawa))
        if message.content == 'Хто я?':
            await message.channel.send('Помидор')
        if message.content == 'Хто ты?':
            await message.channel.send('Зеленский')
        if message.content == 'Где ты?':
            await message.channel.send('Зади тебя')

client = MyClient()
client.run('ODg4NDkwMDUwMzgyMzY0NzAzYUTc1w.UA-urED8mP8eN6uzZIDqyf_HaWM')
