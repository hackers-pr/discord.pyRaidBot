import os

def rbst(random):

  if random!='ry'and random!='rn':
    random='rn'
    
  global number_of_bots

  os.system('del temppy*.py')
  os.system('cls')

  #config check
  config_file=open('cnfg.log', 'r')

  nbots_help=-1
  if config_file.read()=='':
    number_of_bots=int(input('With how many bots you will spam?\n'))
    verify=input('Does the required server have a verification system? (y\n)\n')
    verify_message=input('Now pick a message, what bots will send TO VERIFY.\n')
    message_to_send=input('Now pick a message, what bots will send.\n')
    verify_channel=input('Input verification channel ID.\n')
    message_channel=input('Input needed channel ID (where you will spam).\n')
    token_filename=input('Name a file in rbot folder with tokens\n')
  
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
    if verify=='y':
      temppy.write(temppy.read()+'  ch=client.get_channel('+verify_channel+')\n')
      temppy.write(temppy.read()+'  await ch.send("'+verify_message+'")\n')
    temppy.write(temppy.read()+'  ch=client.get_channel('+message_channel+')\n')
    temppy.write(temppy.read()+'  while True:\n')
    if random=='ry':
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
  
def unchng(eoaou, sthing_to_chng, password):
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
    
def uinfo(member_id, token):
  os.system('del uinfoh.py')
  os.system('cls')
  print('Building uinfoh.py...')
  uinfoh=open('uinfoh.py', 'a+')
  uinfoh.write(uinfoh.read()+'import discord \n')
  uinfoh.write(uinfoh.read()+'from tkinter import *\n')
  uinfoh.write(uinfoh.read()+'import tkinter.messagebox \n')
  uinfoh.write(uinfoh.read()+'client=discord.Client()\n')
  uinfoh.write(uinfoh.read()+'@client.event\n')
  uinfoh.write(uinfoh.read()+'async def on_connect():\n')
  uinfoh.write(uinfoh.read()+'  user=client.get_user('+member_id+')\n')
  uinfoh.write(uinfoh.read()+'  tkinter.messagebox.showinfo("About "+user.name+":", \n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nID: "+str(user.id)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'ndiscriminator: "+user.discriminator+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nbot: "+str(user.bot)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nsystem: "+str(user.system)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nrelationship: "+str(user.relationship)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'ncreated at: "+str(user.created_at)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'navatar url: "+str(user.avatar_url)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nis avatar animated: "+str(user.is_avatar_animated())+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nmention: "+str(user.mention)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nuser color: "+str(user.color)+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nuser is your friend: "+str(user.is_friend())+\n')
  uinfoh.write(uinfoh.read()+'    "\\'+'nuser is blocked: "+str(user.is_blocked()))\n')
  uinfoh.write(uinfoh.read()+'    exit()\n')
  uinfoh.write(uinfoh.read()+'  client.run("'+token+'", bot=False)')
  uinfoh.close()
  print('Running uinfoh.py...')
  os.system('start /min uinfoh.py')
  
def dthelp():
  print('\nSELFBOT COMMANDS:'+
  '\n\nrbst [rn/ry]: start raidbot;'+
  '\nrbtk: taskkill raidbot;'+
  '\nrbcnfg: set rbst config;'+
  '\nunchng [what you need to change, email/avatar/username, password]: change something;'+
  '\nuinfo [user id, token]: shows user info. may not work'
  '\n\nOTHER:'+
  '\n\nhelp: shows this message;'+
  '\nexit: exit.')
  print('\n\n#######################\n'+
  '\nCOMMAND EXAMPLES:\n'+
  '\nrbst ry'+
  '\nhelp'+
  '\nunchng email very_cool@email.com good_password9281'+
  '\nunchng avatar animeavatar.png 02011998'+
  '\nuinfo 527531639019012150 NzNuDI-lEtotally-fake-tokenOd-Ew'+
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
    if len(inpcl)>1:
      rbst(inpcl[1])
  elif inpcl[0]=='unchng':
    if len(inpcl)>3:      
      unchng(eoaou=inpcl[1], sthing_to_chng=inpcl[2], password=inpcl[3])
  elif inpcl[0]=='uinfo':
    if len(inpcl)>2:
      uinfo(inpcl[1], inpcl[2])
