# # Work with Python 3.6
import discord, os, json, time

# TOKEN = os.environ.get('TOKEN')

client = discord.Client()

def save():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'w') as file:
        json.dump(people, file)

people = {"zheka": ""}

with open(os.path.dirname(os.path.realpath(__file__)) + "/save.json", 'r') as file:
    people = json.load(file)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content == "!start_battle":
        people[message.author.id] = ""
        
    if message.content == "!join_":
        people[message.author.id] = ""
    
    if message.author.id in people:
        answer = message.content






    if message.content.startswith('!register'):
        target = None
        for i, n in enumerate(people):
            if n['id'] == message.author.id:
                target = i
        if not bool(target):                
            people.append({"id": message.author.id, "name": message.content.replace("!register", '')})
        else:
            people[target] = {"id": message.author.id, "name": message.content.replace("!register", '')}
            
        save()
        msg = 'Hello ' + message.author.mention + " Який твій улюблений фільм?"
        await message.channel.send(msg) 

    if message.content.startswith('!answer'):
        target = None
        for i, n in enumerate(people):
            if n['id'] == message.author.id:
                target = i

        try:
            people[target]['film'] = message.content.replace('!answer', '')
        except Exception:
            people.append({"id": message.author.id, "film": message.content.replace('!answer', '')})

        save()
        msg = 'Відповідь збережено'
        await message.channel.send(msg) 

    if message.content.startswith('!hello'):
        msg = '!hello ' + message.author.mention
        await message.channel.send(msg)

    if message.content.startswith('!show_all'):
        msg = 'People: \n' + '\n'.join(map(str, people))
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
