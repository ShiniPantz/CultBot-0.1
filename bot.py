import javascript
import os
import time
import helloworld
import values
import random
import json
import messg
import cmd
values.exp=1.5	#set the level cost exponent
values.timer=time.time()
values.timer2=time.time()
values.ttim=random.randint(750,2000)
values.cd={}
values.ccdd=20		#cooldown for gamecommands
jsonfile="SaveFile.json"
with open(jsonfile) as f:
	values.Data=json.load(f)
###################################################################################
#preparing the logfile
if values.Data.get("settings")==None:
	values.Data.update({"settings":{"log":{"number":0,"date":0}}})
x=values.Data["settings"]["log"]["number"]			#filenumber
y=time.strftime("%Y  %B%d %H:%M:%S %A\n", time.localtime())	#firstline
z=time.strftime("%B%d", time.localtime())			#foldername
x+=1								#increases log number
os.makedirs(f"logs/{z}", mode = 0o777, exist_ok = True)		#creates the folder
logs=f"logs/{z}/LogFile{x}.txt"					#set path
with open(logs,"a") as f:
	f.write(f"time={y}")
values.Data["settings"]["log"]["number"]=x
values.Data["settings"]["log"]["date"]=y
with open(jsonfile,"w") as f:
	json.dump(values.Data, f, indent=1)
#####################################################################################
def create_new(name):
	values.Data.update({name:{"logic":{},"items":{"bloccs":{"x":0},"diamond":0,"emerald":0,"xp":0,"level":1}}})
	with open(jsonfile,"w") as f:
		json.dump(values.Data, f, indent=1)
def reroute(olddicc,newdicc,key):
	succ={key:olddicc.pop(key)}
	newdicc.update(succ)
def check_cd(dicc,key,user):	#this function checks cooldown based on values.cd (needs to be passed as dicc), creates new entries if needed, updates values.cd if needed
	if dicc.get(user)==None:
		dicc.update({user:{}})				#guarantees there will always be any cd_info[user]
	if dicc[user].get(key)==None:
		dicc[user].update({key:time.time()})	#updates the cooldown. this can only happen if the cooldown expired
		return(True)
	else:
		if dicc[user].get(key)+values.ccdd<time.time():	#checks if the cooldown expired
			dicc[user].update({key:time.time()})
			return(True)
	return(False)
mineflayer=javascript.require("mineflayer")
bot = mineflayer.createBot({ 'host': helloworld.host,'username': helloworld.username, 'password': helloworld.password ,'auth':'microsoft'})
javascript.once(bot,"spawn")
bot.chat("beep boob")
@javascript.On(bot,"chat")
def public(this, user, message, *rest):
	if user != "whispers":

		if values.timer2+values.ttim<time.time():
			values.timer2=time.time()
			values.ttim=random.randint(750,2000)	#spammer will fire in random intervals between 750 and 2000 seconds
			bot.chat(random.choice((messg.spam1,messg.spam2,messg.spam3,messg.spam4,messg.spam5,messg.spam6,messg.spam7)))


##########################
		print(messg.logpublic(user,message))
		with open(logs,"a") as f:
			f.write(messg.logpublic(user,message)+"\n")
		ucheck=False
		for i in values.Data:
			if i == user:
				ucheck=True
		if not ucheck:
			create_new(user)
###########################






#####
#####
		C_message=None
		text=None
		if user!="CultBot":
			C_message=cmd.findC_(message)				#C_message="test1_abc"
#####
		if C_message!=None:
			list_cw=cmd.cmdlist_chat_whisper
			list_cc=cmd.cmdlist_chat_chat
			list_ww=cmd.cmdlist_whisper_whisper
			list_wc=cmd.cmdlist_whisper_chat
			string_cw=cmd.findcmd(C_message,list_cw)			#string=(test1,"test1","abc")	#the important part here is !!list_cw!! getting passed into cmd.findcmd() as the second argument
			string_cc=cmd.findcmd(C_message,list_cc)
			string_wc=cmd.findcmd(C_message,list_wc)
			string_ww=cmd.findcmd(C_message,list_ww)
			cd_info=values.cd

			if string_cw!=None:					#commands from that library object get the result printed by the bot in CHAT
				funct,cmdcmd,cmdarg=string_cw
				
				if check_cd(cd_info,cmdcmd,user):		#checks for cooldown
					text=funct(user,cmdarg)
					if text!=None:
						bot.chat(text)
				else:
					cooldd=str(int(cd_info[user][cmdcmd]+values.ccdd-time.time()))
					bot._client.write("chat",{"message":f"/w {user} "+" cooldown="+cooldd})
			elif string_cc!=None:
				funct,cmdcmd,cmdarg=string_cc
				bot.chat(funct(user,cmdarg))

#######################################################################################################################
#######################################################################################################################
@javascript.On(bot,"whisper")
def whisper(this, user, message, a1, *rest):
	message=message[:-1]		#removes the last " " from message
#######################
	ucheck=False
	for i in values.Data:
		if i == user:
			ucheck=True
	if not ucheck:
		create_new(user)
#######################
	print(messg.logprivate(user,message))
	with open(logs,"a") as f:
		f.write(messg.logpublic(user,message)+"\n")
	if True:
		C_message=None
		text=None
		if user!="CultBot":
			C_message=cmd.findC_(message)				#C_message="test1_abc"
#####
		if C_message!=None:
			list_cw=cmd.cmdlist_chat_whisper
			list_cc=cmd.cmdlist_chat_chat
			list_ww=cmd.cmdlist_whisper_whisper
			list_wc=cmd.cmdlist_whisper_chat
			string_cw=cmd.findcmd(C_message,list_cw)			#string=(test1,"test1","abc")	#the important part here is !!list_cw!! getting passed into cmd.findcmd() as the second argument
			string_cc=cmd.findcmd(C_message,list_cc)
			string_wc=cmd.findcmd(C_message,list_wc)
			string_ww=cmd.findcmd(C_message,list_ww)
			cd_info=values.cd

			if string_cw!=None:					#commands from that library object get the result printed by the bot in CHAT
				funct,cmdcmd,cmdarg=string_cw
				if check_cd(cd_info,cmdcmd,user):		#checks for cooldown
					text=funct(user,cmdarg)
					if text!=None:
						bot._client.write("chat",{"message":f"/w {user} "+text})
				else:
					cooldd=str(int(cd_info[user][cmdcmd]+values.ccdd-time.time()))
					bot._client.write("chat",{"message":f"/w {user} "+" cooldown="+cooldd})
			elif string_cc!=None:
				funct,cmdcmd,cmdarg=string_cc
				bot.chat(funct(user,cmdarg))

#############################################################################################################################################
#############################################################################################################################################
#
@javascript.On(bot,"kicked")
def xxkick(this,reason,loggedIn,*rest):
	bot.quit("")
	exit()
@javascript.On(bot,"end")
def xxend(this,reason,*rest):
	bot.quit("")
	exit()




#for i in range(100):
#    time.sleep(10)
#    bot.chat(">>>lol I'm a bot, this is message # "+str(i))
#print("5")
