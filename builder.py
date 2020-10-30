import os

os.system('del temppy*.py')
os.system('cls')

nbots_help=0
number_of_bots=int(input('With how many bots you will spam?\n'))
message_to_send=input('Now pick a message, what bots will send.\n')

for x in range(number_of_bots):
  nbots_help+=1
  temppy=open('temppy'+str(nbots_help)+'.py', 'a+')
  temppy.write('import discord; client=discord.Client()\n')
  token_filename=input('Name a file in rbot folder with №'+str(nbots_help)+' bot token')
  token_file=open(token_filename, 'r')
  token=token_file.read()
  token_file.close()
  temppy.write(temppy.read()+'@client.event\n')
  temppy.write(temppy.read()+'async def on_message(message):\n')
  temppy.write(temppy.read()+'  if message.content=="rbot%run":\n')
  temppy.write(temppy.read()+'    while True:\n')
  temppy.write(temppy.read()+'      await message.channel.send("'+message_to_send+'")\n')
  temppy.write(temppy.read()+'client.run("'+token+'", bot=False)\n')
  temppy.close()
  print('The settings of the №'+str(nbots_help)+' bot were written')

nbots_help=0 
print('Settings done, starting bot...')

for x in range(number_of_bots):
  nbots_help+=1
  os.system('start /min temppy'+str(nbots_help)+'.py')
  