import os
import discord
from Ocul_Persistance import keep_alive

#Values to Keep
client = discord.Client()
TOKEN = os.environ['token']
mode = ""


#Method to get Mode to enter
async def setStatus(x):
  global mode
  goodInputs = ["1","operational","2","development","3","Silent","4","shutdown"]
  botStatus = str(x)
  
  while(botStatus not in goodInputs):
    botStatus = input("\nCommand:\n1. Operational\n2. Development\n3. Silent\n4. Shutdown\n\n").lower()
  
  #Operational
  if(botStatus=="1" or botStatus.lower()=="operational"):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "you"), status=discord.Status.online)
    mode = "operational"
    print("Operational Status Deployed")
  
  #Development
  elif(botStatus=="2" or botStatus.lower()=="development"):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "only my developer"), status=discord.Status.idle)
    mode = "development"
    print("Development Status Deployed")
  
  #Silent Mode
  elif(botStatus=="3" or botStatus.lower()=="silent"):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "no one"), status=discord.Status.dnd)
    mode = "silent"
    print("Silent Status Deployed")
  
  #Shutdown
  else:
    await client.close()
    mode = "shutdown"
    print("Shutdown")

#Method on startup of Bot
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await setStatus("")
  
  
#Method on getting message
@client.event
async def on_message(message):
  #Check Silent or Development mode
  if mode == "silent" or (mode == "development" and message.author.id != os.environ['developer_id']):
    return

  #Don't take input from bot itself (no pesky recursion xD)
  if message.author == client.user:
    return
  
  if message.content.startswith('o!'):
    await message.channel.send('Hello!')

#Run Ocul and make sure it is going to stay up
keep_alive()
client.run(TOKEN)