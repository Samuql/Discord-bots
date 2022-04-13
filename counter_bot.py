import discord
import json

keywords = ["word1", "word2", "word3"]


class MyClient(discord.Client):

    # bot login
    async def on_ready(self):
        print("Bot online")

    def get_score(self, member: discord.Member):
        with open("users.json") as users:
            dictlist = json.load(users)

        id = str(member.id)
        for k in dictlist:
            if k == id:
                return dictlist[k]  # return val corresponding to id

    def add_score(self, member: discord.Member, amount: float):
        with open("users.json") as jsonFile:
            dictlist = json.load(jsonFile)

        id = str(member.id)
        if id not in dictlist:
            dictlist[id] = amount  # create new dict entry for user
        else:
            dictlist[id] += amount
        new = dictlist

        with open("users.json", "w+") as dictlist:
            json.dump(new, dictlist, sort_keys=True, indent=4)  # save the changes

    # When a message is sent
    async def on_message(self, message):
        if message.author != client.user:
            author = message.author
            if message.content in keywords:
                self.add_score(author, 0.01)
                await message.channel.send(
                    message.content + " ??? " + author.mention + " Must pay 1ct." + author.name
                    + "'s debts are now " + str(round(self.get_score(author), 3)) + "€!")


client = MyClient()
client.run("TOKEN")
