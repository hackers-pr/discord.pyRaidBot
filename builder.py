import os
import os.path
os.system('cd temp')

def rbst(token_filename, random):

  if random!='random'and random!='normal':
    random='normal'
    
  global number_of_bots

  os.system('del temppy*.py')
  os.system('cls')

  #config check
  config_file=open('cnfg.log', 'r')

  nbots_help=-1
  if config_file.read()=='':
    number_of_bots=int(input('With how many bots you will spam?\n'))
    message_to_send=input('Now pick a message, what bots will send.\n')
    message_channel=input('Input needed channel ID (where you will spam).\n')
  
  else:
    config_file=open('cnfg.log', 'r')
    cfgr=str(config_file.read())
    config_list=list(cfgr.split(' '))
    number_of_bots=int(config_list[0])
    verify=config_list[1]
    verify_message=config_list[2]
    message_to_send=config_list[3]
    verify_channel=config_list[4]
    message_channel=config_list[5]
    token_filename=config_list[6]
    
  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()

  for x in range(number_of_bots):
    nbots_help+=1
    temppy=open('temppy'+str(nbots_help)+'.py', 'a+')
    temppy.write('import discord; import string; import random; client=discord.Client()\n')
    temppy.write(temppy.read()+'@client.event\n')
    temppy.write(temppy.read()+'async def on_connect():\n')
    temppy.write(temppy.read()+'  text=""\n')
    temppy.write(temppy.read()+'  ch=client.get_channel('+message_channel+')\n')
    temppy.write(temppy.read()+'  while True:\n')
    if random=='random':
      temppy.write(temppy.read()+'      for x in range(1999):\n')
      temppy.write(temppy.read()+'        text+=random.choice(string.ascii_letters)\n')
      temppy.write(temppy.read()+'      await ch.send(text)\n')
      temppy.write(temppy.read()+'      text=""\n')
    else:
      temppy.write(temppy.read()+'    await ch.send("'+message_to_send+'")\n')
    temppy.write(temppy.read()+'client.run("'+token[nbots_help]+'", bot=False)\n')
    temppy.close()
    print('The settings of the №'+str(nbots_help+1)+' bot were written')

  nbots_help=-1
  print('Settings done, starting bot...')

  for x in range(number_of_bots):
    nbots_help+=1
    os.system('start /min temppy'+str(nbots_help)+'.py')

def verify(token_filename, versystem):

  nbots_help=-1

  os.system('del verpy*.py')
  os.system('cls')
  
  verify_channel=input('Input verification channel ID.\n')
  if versystem=='message':
    verify_message=input('Now pick a message, what bots will send to verify.\n')
  number_of_bots=int(input('How many bots you need to verify?\n'))
    
  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()
  
  for x in range(number_of_bots):
  
    nbots_help+=1
    verpy=open('verpy'+str(nbots_help)+'.py', 'a+')   
    verpy.write('import discord; client=discord.Client()\n')
    verpy.write(verpy.read()+'@client.event\n')
    verpy.write(verpy.read()+'async def on_connect():\n')
    verpy.write(verpy.read()+'  ch=client.get_channel('+verify_channel+')\n')
    verpy.write(verpy.read()+'  await ch.send("'+verify_message+'")\n')
    verpy.write(verpy.read()+'  exit()\n')
    verpy.write(verpy.read()+'client.run("'+token[nbots_help]+'", bot=False)\n')
    verpy.close()
    print('The settings of the №'+str(nbots_help+1)+' bot were written')

  nbots_help=-1
  print('Settings done, starting bot...')  
    
  for x in range(number_of_bots):
    nbots_help+=1
    os.system('start /min verpy'+str(nbots_help)+'.py')
  
def rbtk():
  try:
    number_of_bots
  except:
    number_of_bots=int(input('How many bots you need to kill?\n'))
  nbots_help=-1
  for x in range(number_of_bots):
    nbots_help+=1
    os.system('taskkill /f /im temppy'+str(nbots_help)+'.py')

def rbcnfg():
  os.system('cd ..')
  
  global number_of_bots

  config_file=open('cnfg.log', 'w')
  number_of_bots=int(input('With how many bots you will spam?\n'))
  verify=input('Does the required server have a verification system? (y\n)\n')
  verify_message=input('Now pick a message, what bots will send TO VERIFY.\n')
  message_to_send=input('Now pick a message, what bots will send.\n')
  verify_channel=input('Input verification channel ID.\n')
  message_channel=input('Input needed channel ID (where you will spam).\n')
  token_filename=input('Name a file in rbot folder with bots token\n') 
  config_file.write(str(number_of_bots)+' '+verify+' '+verify_message+' '+message_to_send+' '+verify_channel+' '+message_channel+' '+token_filename)
  
  os.system('cd temp')
  
def unchng(eoaou, sthing_to_chng, password):
  os.system('del usch*.py')
  os.system('cls')

  if eoaou!='email' and eoaou!='avatar' and eoaou!='username':
    print('error: please input, what you want to change')
    return
  nbots_help=-1
  number_of_bots=int(input('For how many bots you will change username?\n'))
  token_filename=input('Name a file in rbot folder with tokens\n')
  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()
  for x in range(number_of_bots):
    nbots_help+=1
    usern_change=open('usch'+str(nbots_help)+'.py', 'a+')
    usern_change.write('import discord; from tkinter import *; import tkinter.messagebox; client=discord.Client()\n')
    usern_change.write('@client.event\n')
    usern_change.write(usern_change.read()+'async def on_connect():\n')
    usern_change.write(usern_change.read()+'  user=client.user\n')
    if eoaou=='avatar':
      usern_change.write(usern_change.read()+'  avatar=open("'+sthing_to_chng+'", "rb").read()\n')
      usern_change.write(usern_change.read()+'  try:\n')
      usern_change.write(usern_change.read()+'    await user.edit('+eoaou+'=avatar,password="'+password+'")\n')
      usern_change.write(usern_change.read()+'    exit()\n')
      usern_change.write(usern_change.read()+'  except HTTPException:\n')
      usern_change.write(usern_change.read()+'    tkinter.messagebox.showinfo("Warning", "Something went wrong... Maybe you change your avatar too fast!")\n')
      usern_change.write(usern_change.read()+'    exit()\n')
    else:
      usern_change.write(usern_change.read()+'  try:\n')
      usern_change.write(usern_change.read()+'    await user.edit('+eoaou+'="'+sthing_to_chng+'",password="'+password+'")\n')
      usern_change.write(usern_change.read()+'    exit()\n')
      usern_change.write(usern_change.read()+'  except HTTPException:\n')
      usern_change.write(usern_change.read()+'    tkinter.messagebox.showinfo("Warning", "Something went wrong... Maybe you change your nickname/email too fast!")\n')
      usern_change.write(usern_change.read()+'    exit()\n')
    usern_change.write(usern_change.read()+'client.run("'+token[nbots_help]+'", bot=False)\n')
    usern_change.close()

  nbots_help=-1

  for x in range(number_of_bots):
    nbots_help+=1
    os.system('start /min usch'+str(nbots_help)+'.py')
  
def dthelp():
  print('\nSELFBOT COMMANDS:'+
  '\n\nrbst [file with tokens name] [random/normal]: start raidbot;'+
  '\nrbtk: taskkill raidbot;'+
  '\nrbcnfg: set rbst config;'+
  '\nunchng [what you need to change, email/avatar/username, password]: change something;'+
  '\n\nOTHER:'+
  '\n\nhelp: shows this message;'+
  '\nexit: exit.')
  print('\n\n#######################\n'+
  '\nCOMMAND EXAMPLES:\n'+
  '\nrbst bots.txt random'+
  '\nverify tokens.log message'+
  '\nhelp'+
  '\nunchng email very_cool@email.com good_password9281'+
  '\nunchng avatar animeavatar.png 02011998'+
  '\n\nMore examples will come with more commands!')

print("print help if you don't know what to do ― hackers_pr")

while 1:
  inpc=input()
  inpcl=list(inpc.split(' '))
  if inpc=='rbtk':
      rbtk()
  elif inpc=='rbcnfg':
      rbcnfg()
  elif inpc=='help':
      dthelp()
  elif inpc=='exit':
      exit()    
  elif inpcl[0]=='rbst':
    if len(inpcl)>2:
      rbst(inpcl[1], inpcl[2])
    else:
      print('not enough args')
  elif inpcl[0]=='unchng':
    if len(inpcl)>3:      
      unchng(eoaou=inpcl[1], sthing_to_chng=inpcl[2], password=inpcl[3])
    else:
      print('not enough args')
  elif inpcl[0]=='verify':
    if len(inpcl)>2:
      verify(inpcl[1], inpcl[2])
  else:
    print('unknown command')
