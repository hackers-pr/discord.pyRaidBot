import os
import json
import threading
import subprocess
from time import *

global bot_procs
bot_procs=[]

def rbst(token_filename, random, config_filename):

  if random!='random' and random!='normal':
    random='normal'
    
  global number_of_bots
  del_help=0

  while True:
    try:
      os.remove('temppy'+str(del_help)+'.py')
      del_help+=1
    except FileNotFoundError:
      break
  
  nbots_help=-1
  if config_filename.lower()=='none':
    number_of_bots=int(input('With how many bots you will spam?\n'))
    message_to_send=input('Now pick a message, what bots will send.\n')
    message_channel=input('Input needed channel ID (where you will spam).\n')
  
  else:
    config=open(config_filename+'.json','r')
    cfg=json.loads(config.read())
    number_of_bots=cfg['number_of_bots']
    message_to_send=cfg['message_to_send']
    message_channel=cfg['message_channel']
    
  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()

  for x in range(number_of_bots):
    nbots_help+=1
    temppy=open('temppy'+str(nbots_help)+'.py', 'a+')
    temppy.write('''import discord; import string; import random; client=discord.Client()
@client.event
async def on_connect():
  text=""
  ch=client.get_channel('''+str(message_channel)+''')
  while True:'''+'\n')
    if random=='random':
      temppy.write(temppy.read()+'''      for x in range(1999):
        text+=random.choice(string.ascii_letters)
      await ch.send(text)
      text=""'''+'\n')
    else:
      temppy.write(temppy.read()+'    await ch.send("'+str(message_to_send)+'")'+'\n')
    temppy.write('client.run("'+token[nbots_help]+'", bot=False)')
    temppy.close()
    print('The settings of the №'+str(nbots_help+1)+' bot were written')

  nbots_help=-1
  print('Settings done, starting bot...')

  for x in range(number_of_bots):
    nbots_help+=1
    bot_procs.append(subprocess.Popen(('python3 -u temppy'+str(nbots_help)+'.py').split()))

def verify(token_filename, versystem, config_filename):

  if versystem!='message' and versystem!='reaction':
    print('invalid argument')
    return

  nbots_help=-1
  del_help=0

  while True:
    try:
      os.remove('verpy'+str(del_help)+'.py')
      del_help+=1
    except FileNotFoundError:
      break
  
  if config_filename.lower()=='none': 
    verify_channel=input('Input verification channel ID.\n')
    if versystem=='message':
      verify_message=input('Now pick a message, what bots will send to verify.\n')
    elif versystem=='reaction':
      verify_reaction_id=input('Please, input reaction ID.\n')
      reaction_message_id=input('Now enter the message ID, where you will add the reaction.\n')
    number_of_bots=int(input('How many bots you need to verify?\n'))
  
  else:
    config=open(config_filename+'.json','r')
    cfg=json.loads(config.read())
    verify_channel=cfg['verify_channel']
    if versystem=='message':
      verify_message=cfg['verify_message']
    elif versystem=='reaction':
      verify_reaction_id=cfg['verify_reaction_id']
      reaction_message_id=cfg['reaction_message_id']
    number_of_bots=cfg['number_of_bots']
  
  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()
  
  for x in range(number_of_bots):  
    nbots_help+=1
    verpy=open('verpy'+str(nbots_help)+'.py', 'a+')   
    verpy.write('''import discord; client=discord.Client()
@client.event
async def on_connect():
  ch=client.get_channel('''+str(verify_channel)+')\n')
    if versystem=='message':
      verpy.write(verpy.read()+'  await ch.send("'+str(verify_message)+'")\n')
    elif versystem=='reaction':
      verpy.write(verpy.read()+'  ej=client.get_emoji('+str(verify_reaction_id)+''')
  async for message in ch.history(limit=100):
    if message.id=='''+str(reaction_message_id)+''':
      await message.add_reaction(ej)'''+'\n')
    verpy.write(verpy.read()+'client.run("'+token[nbots_help]+'", bot=False)\n')
    verpy.close()
    print('The settings of the №'+str(nbots_help+1)+' bot were written')

  nbots_help=-1
  print('Settings done, starting bot...')  
    
  for x in range(number_of_bots):
    nbots_help+=1
    bot_procs.append(subprocess.Popen(('python3 -u verpy'+str(nbots_help)+'.py').split(), 
    stderr=subprocess.PIPE))
  
def rbtk():
  for x in range(len(bot_procs)):
    bot_procs[0].kill()
    bot_procs.pop(0)

def cnfg():
  
  config_filename=input('Please, enter config filename to edit or create new config.\n')
  config=open(config_filename+'.json','a')
  
  str_config=''
  variable_name=''
  variable_value=''
  variable_type=''
  
  while True:
    variable_name=input('Variable name:\n')
    if variable_name=='q':
      break
    variable_value=input('Variable value:\n')
    if variable_value=='q':
      break
    variable_type=input('Variable type: (int/str)\n')
    if variable_type=='q':
      break
    if variable_type.lower()=='int':
      str_config+='"'+variable_name+'": int('+variable_value+'),'
    elif variable_type.lower()=='str':
      str_config+='"'+variable_name+'": "'+variable_value+'",'
    else:
      print('error: unknown variable type')
    
  if str_config!='':
    print('config.write(json.dumps({'+str_config+'},sort_keys=True,indent=4))')
    eval('config.write(json.dumps({'+str_config+'},sort_keys=True,indent=4))')
  
def unchng(eoaou, sthing_to_chng, password, config_filename):

  del_help=0

  while True:
    try:
      os.remove('usch'+str(del_help)+'.py')
      del_help+=1
    except FileNotFoundError:
      break

  if eoaou!='email' and eoaou!='avatar' and eoaou!='username':
    print('error: please input, what you want to change')
    return
  nbots_help=-1

  if config_filename.lower()=='none':
    number_of_bots=int(input('For how many bots you will change username?\n'))
    token_filename=input('Name a file in rbot folder with tokens\n')

  else:
    config=open(config_filename+'.json','r')
    cfg=json.loads(config.read())
    number_of_bots=cfg['number_of_bots']
    token_filename=cfg['token_filename']

  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()
  for x in range(number_of_bots):
    nbots_help+=1
    usern_change=open('usch'+str(nbots_help)+'.py', 'a+')
    usern_change.write('''import discord; client=discord.Client()
@client.event
async def on_connect():
  user=client.user'''+'\n')
    if eoaou=='avatar':
      usern_change.write(usern_change.read()+'  avatar=open("'+sthing_to_chng+'''", "rb").read()
  try:
    await user.edit('''+eoaou+'=avatar,password="'+password+'''")
  except:
    print("\\nWarning!\\n*****\\nSomething went wrong... Maybe you change your avatar too fast!\\n")'''+'\n')
    else:
      usern_change.write(usern_change.read()+'''  try:
    await user.edit('''+eoaou+'="'+sthing_to_chng+'",password="'+password+'''")
  except HTTPException:
    print("\\nWarning!"\n*****\nSomething went wrong... Maybe you change your nickname/email too fast!\\n"')'''+'\n')
    usern_change.write(usern_change.read()+'client.run("'+token[nbots_help]+'", bot=False)\n')
    usern_change.close()

  nbots_help=-1

  for x in range(number_of_bots):
    nbots_help+=1
    bot_procs.append(subprocess.Popen(('python3 -u usch'+str(nbots_help)+'.py').split()))
 
def tokencheck(token_filename, config_filename):

  del_help=0

  while True:
    try:
      os.remove('tokencheck'+str(del_help)+'.py')
      del_help+=1
    except FileNotFoundError:
      break

  if config_filename.lower()=='none':
    number_of_bots=int(input('How many accounts you will check?\n'))

  else:
    config=open(config_filename+'.json','r')
    cfg=json.loads(config.read())
    number_of_bots=cfg['number_of_bots']

  token_file=open(token_filename, 'r')
  token=token_file.read().split(' ')
  token_file.close()

  for x in range(number_of_bots):
    tokencheck=open('tokencheck'+str(x)+'.py', 'a+')
    tokencheck.write('''import discord; client=discord.Client()
@client.event
async def on_ready():
  friends=''
  blocked=''
  print('INFO ABOUT '+client.user.name+'#'+str(client.user.discriminator)+':\\n\\
email:'+str(client.user.email)+'\\n\\
id:'+str(client.user.id)+'\\n\\
language:'+str(client.user.locale)+'\\n\\
mfa enabled:'+str(client.user.mfa_enabled)+'\\n\\
have nitro:'+str(client.user.premium)+'\\n\\
nitro type:'+str(client.user.premium_type)+'\\n\\n\\
*******************\\n')
  for x in client.user.friends:
    friends+=x.name+'\\n\'
  for x in client.user.blocked:
    blocked+=x.name+'\\n\'
  print('friends:\\n'+str(friends)+'\\n\\
*******************\\n\\
blocked:\\n'+str(blocked)+'\\n')
client.run("'''+token[x]+'", bot=False)')
    tokencheck.close()

  for x in range(number_of_bots):
    bot_procs.append(subprocess.Popen(('python3 -u tokencheck'+str(x)+'.py').split()))

def dthelp():
  print('\nSELFBOT COMMANDS:'+
  '\n\nrbst [file with tokens name] [random/normal] [config filename]: start raidbot;'+
  '\nverify [file with tokens name] [verify system (message/reaction)] [config filename]: passing verify;'+
  '\nrbtk: taskkill raidbot;'+
  '\ncnfg: set config;'+
  '\nunchng [what you need to change] [email/avatar/username] [password] [config filename]: changes something;'+
  '\ntokencheck [file with tokens name] [config filename];'+
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
  elif inpc=='cnfg':
      cnfg()
  elif inpc=='help':
      dthelp()
  elif inpc=='exit':
      exit()    
  elif inpcl[0]=='rbst':
    if len(inpcl)>3:
      rbst(inpcl[1], inpcl[2], inpcl[3])
    elif len(inpcl)==3:
      rbst(inpcl[1], inpcl[2], 'none')
    else:
      print('not enough args')
  elif inpcl[0]=='unchng':
    if len(inpcl)==4:      
      unchng(eoaou=inpcl[1], sthing_to_chng=inpcl[2], password=inpcl[3], config_filename='none')
    elif len(inpcl)>4:
      unchng(eoaou=inpcl[1], sthing_to_chng=inpcl[2], password=inpcl[3], config_filename=inpcl[4])
    else:
      print('not enough args')
  elif inpcl[0]=='verify':
    if len(inpcl)>3:
      verify(inpcl[1], inpcl[2], inpcl[3])
    elif len(inpcl)==3:
      verify(inpcl[1], inpcl[2], 'none')
  elif inpcl[0]=='tokencheck':
    if len(inpcl)>2:
      tokencheck(inpcl[1], inpcl[2])
    elif len(inpcl)==2:
      tokencheck(inpcl[1], 'none')
  else:
    print('unknown command')
