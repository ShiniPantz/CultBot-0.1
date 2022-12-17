import json
import messg
import values
import random
import time
jsonfile="SaveFile.json"
with open(jsonfile) as f:
	values.Data=json.load(f)
#############################################################
def save_me():		
	with open(jsonfile,"w") as f:
		json.dump(values.Data, f, indent=1)
def load_me():
	with open(jsonfile) as f:
		values.Data=json.load(f)
def create_new(name):
	values.Data.update({name:{"logic":{},"items":{"bloccs":{"x":0},"diamond":0,"emerald":0,"xp":0,"level":1}}})
	with open(jsonfile,"w") as f:
		json.dump(values.Data, f, indent=1)
def findcmd(x,cmdl):					#x=test_abc cmdl={"test0":test0,"test1":test1,"test2":test2}
	for i in cmdl:
		if x.startswith(i):			
			return(cmdl.get(i),x[:len(i)+1],x[len(i)+1:])
def findC_(x):						#x="C_test1_abc"
	check=x.find("C_")
	check2=x.find("] C_")
	check3=x.find("c_")
	if check<0:					#checks if "C_" exists anywhere in the message
		return(None)
	elif check==0:
		return(x.split("C_",maxsplit=1)[1])		#returns "test1_abc"
	elif check3==0:
		return(x.split("c_",maxsplit=1)[1])		#returns "test1_abc"
	elif check2<0:
		return(None)
	else:
		return(x.split("C_",maxsplit=1)[1])
def create_new_item(user,item,startvalue):
	if values.Data[user]["items"].get(item)==None:		#checks if Item exists in the player object
		values.Data[user]["items"].update({item:startvalue})
		save_me()
def create_new_logic(user,logic,startvalue):
	if values.Data[user]["logic"].get(logic)==None:		#checks if Item exists in the player object
		values.Data[user]["logic"].update({logic:startvalue})
		save_me()
def update_decay(user):
	if values.Data[user]["items"].get("dxp")==None:		#when dxp don't yet exist in the playerobject
		create_new_item(user,"dxp",0)	
		create_new_logic(user,"dxp",[int(time.time()),False])	#the second value makes sure, before leveling up you can't access "C_level_dxp"
	a=values.Data[user]["items"]["dxp"]	#dxp amount
	b,c=values.Data[user]["logic"]["dxp"]	#time and True/False
	##################
	mx=values.Data[user]["items"].get("matter")
	if mx==None:
		mx=1
	lvv=values.Data[user]["items"]["level"]
	basedxp=a			#dxp amount before adding leftover xp and substracting decay
	decay=(int(time.time())-b)*lvv*mx
	finaldxp=basedxp-decay
	if finaldxp<0:
		finaldxp=0
		decay=basedxp				#if decay is greater than all dxp, I get as many diamonds as there is dxp
	values.Data[user]["items"]["dxp"]=finaldxp
	values.Data[user]["logic"]["dxp"]=[int(time.time()),c]
	values.Data[user]["items"]["diamond"]+=decay
def level_up(user):
	lvv=values.Data[user]["items"]["level"]
	xp=values.Data[user]["items"]["xp"]
	exp=values.exp
	adddxp=int(xp-(100*lvv+(exp**lvv)))			#leftover xp after levelup
	update_decay(user)
	values.Data[user]["items"]["dxp"]+=adddxp
	values.Data[user]["items"]["level"]+=1
	values.Data[user]["items"]["xp"]=0
def level_up_dxp(user):
	update_decay(user)
	lvv=values.Data[user]["items"]["level"]
	dxp=values.Data[user]["items"]["dxp"]
	exp=values.exp
	if values.Data[user]["items"]["dxp"]>=100*lvv+(exp**lvv):
		while values.Data[user]["items"]["dxp"]>0:
			lvv=values.Data[user]["items"]["level"]
			dxp=values.Data[user]["items"]["dxp"]
			exp=values.exp
			adddxp=int(dxp-(100*lvv+(exp**lvv)))			#leftover dxp after levelup
			values.Data[user]["items"]["dxp"]=adddxp
			values.Data[user]["items"]["level"]+=1
		values.Data[user]["items"]["dxp"]=0
	else:
		values.Data[user]["items"]["xp"]+=dxp
		values.Data[user]["items"]["dxp"]=0
def resetfile(user):
	values.Data.pop(user)
	create_new(user)
def calc_bloccs(user):	#returns x=sum and y=product of all blocc
	x=0
	y=1
	for i in values.Data[user]["items"]["bloccs"]:
		x+=values.Data[user]["items"]["bloccs"][i]
		y*=values.Data[user]["items"]["bloccs"][i]+1
	return(x,y)
def calc_prestige(user):
	return(values.Data[user]["items"]["matter"]*values.Data[user]["items"]["antimatter"]*-1)
######################################################################################################
######################################################################################################
def mine_(user,text):
	update_decay(user)
	blccnum=calc_bloccs(user)
	btype="diamond"
	if random.randint(1,5)==1:
		btype="emerald"
	print(blccnum)
	if btype=="diamond":
		mined=random.randint(1,5)*blccnum[1]	#diamond bonus is multiple of all blocc
	elif btype=="emerald":
		mined=random.randint(1,5)*blccnum[0]	#emerald bonus is adding of all blocc
	values.Data[user]["items"][btype]+=mined	#	
	save_me()
	return(messg.mininh(user,mined,btype))
def craft_(user,text):
#cost=9,888,77777,6666666  rxturn=1,2,4,8
	blocctypes=["x","Dirt","Iron","Obsidian","Beacon"]
	cost=8			#if cost get's changed, text is a valid argument
	cl=values.Data[user]["logic"].get("craftlevel")
	if cl==None:
		cl=0
	cl+=1
	for i in blocctypes:
		if i==text:	
			if values.Data[user]["items"]["bloccs"].get(text)==None:	#checks if text exists in the playerobject
				values.Data[user]["items"]["bloccs"].update({text:0})	#if not, it creates it
			if i=="x" and cl>0:
				cost=9
				rxturn=1
			elif i=="Dirt" and cl>1:
				cost=888
				rxturn=2
			elif i=="Iron" and cl>2:
				cost=77777
				rxturn=4
			elif i=="Obsidian" and cl>3:
				cost=6666666
				rxturn=8
			elif i=="Beacon" and cl>4:
				cost=555555555
				rxturn=16
	if cost==8:		#text was not a valid argument as cost is still 8, default is x_blocc
		cost=9
		text="x"
		rxturn=1
	update_decay(user)
	exp=values.exp
	lvv=values.Data[user]["items"]["level"]			#lvv bll x1 and x2 get declared before the calculation
	dia=values.Data[user]["items"].get("diamond")
	x1=values.Data[user]["items"].get("matter")
	x2=values.Data[user]["items"].get("antimatter")
	dxp=values.Data[user]["items"].get("dxp"),values.Data[user]["logic"].get("dxp")
	if x1==None:
		x1=1
		x2=-1
	if dxp==None:
		dxp=[0,0,False]
	if values.Data[user]["items"]["diamond"]>=cost*values.Data[user]["items"]["level"]:	#checks if you are able to craft
		print(dia,lvv,x1,x2)
		
		values.Data[user]["items"]["xp"]+=(dia-(cost*lvv))*x1*x2*-1		#player object gets modified
		values.Data[user]["items"]["diamond"]=0
		values.Data[user]["items"]["bloccs"][text]+=rxturn*lvv
		if values.Data[user]["items"]["xp"]>=100*lvv+(exp**lvv):	#checks for level-up
			level_up(user)
			values.Data[user]["logic"]["dxp"][1]=True	#setting the third value to "True" makes sure you are able to use "C_level_dxp" after the first level up
		save_me()						#json gets updated
		return(messg.craff(user,lvv,dia,x1,x2,cost,rxturn,text))			#returns chatmessage
	else:												
		return(messg.craff0(user,lvv,cost,rxturn,text))	#craft check failed, nothing happens
def prestige_(user,message):
	if values.Data[user]["items"].get("antimatter")==None:
		create_new_item(user,"matter",1)
		create_new_item(user,"antimatter",-1)
	ppq=message.split(" ")[0]	#"123C_prestige12345 8765C_2876jsbgj" -> "2345"
	if ppq.isnumeric()==True:
		ppq=int(ppq)
		levv=values.Data[user]["items"]["level"]
		if ppq>levv and levv>5:
			return(messg.prestige1(levv))
		elif levv<5 or ppq<5:
			return(messg.prestige2)
		###########################################################
		elif levv>4 and levv>ppq-1:
			values.Data[user]["items"]["diamond"]=0
			values.Data[user]["items"]["xp"]=0
			values.Data[user]["items"]["bloccs"]={"x":0}
			values.Data[user]["items"]["level"]=1
			values.Data[user]["items"]["antimatter"]-=ppq
			values.Data[user]["items"]["matter"]=levv-ppq+1
			save_me()
			matter=values.Data[user]["items"]["matter"]
			antimatter=values.Data[user]["items"]["antimatter"]
			logic=int(matter/20)
			values.Data[user]["logic"].update({"craftlevel":logic})
			return(messg.prestige3(user,matter,antimatter))
		#############################################################
		else:
			return(messg.brokenlol)
	else:
		return(messg.prestige4)
def sacrifice_(user,text):
	if values.Data[user]["items"]["level"]>99:
		if values.Data[user]["items"].get("xp_bottle")==None:
			resetfile(user)
			create_new_item(user,"xp_bottle",1)
			return(messg.sac1st(user))
		else:
			bttl=values.Data[user]["items"].get("xp_bottle")+1
			resetfile(user)
			create_new_item(user,"xp_bottle",bttl)
			return(messg.sac(user,bttl))
	return(messg.sacno)
def inv_(user,hhh):
	update_decay(user)			#
	hhh=hhh.split(" ")[0]
	if hhh=="bloccs":
		x,y=calc_bloccs(user)
		return(messg.xinv_blcc(user,x,y))
	elif hhh=="prestige":
		return(messg.xinv_prestige(user,calc_prestige(user),values.Data[user]["items"]["matter"],values.Data[user]["items"]["antimatter"]))
	for i in values.Data[user]["items"]:
		if hhh==i:
			x=values.Data[user]["items"][hhh]
			return(messg.xinv(user,x,hhh))
	for j in values.Data[user]["items"]["bloccs"]:
		if hhh==j:
			x=values.Data[user]["items"]["bloccs"][hhh]
			return(messg.xinv_singleblcc(user,x,hhh))
	return(messg.xinv_fail(user,hhh))
def index_(user,ixx):
	return(messg.newhelp)
def level_(user,text):
	update_decay(user)
	lvv=values.Data[user]["items"]["level"]
	xp=values.Data[user]["items"]["xp"]
	exp=values.exp
	if text.startswith("dxp"):
		if values.Data[user]["items"].get("dxp")!=None:			#itemexistence check
			if values.Data[user]["logic"].get("dxp")[1]:		#levelup check
				dxp=values.Data[user]["items"].get("dxp")
				mx=values.Data[user]["items"].get("matter")
				if mx==None:
					mx=1
				return(messg.dlvv(user,dxp,lvv,mx))
	return(messg.levelss(user,lvv,xp,exp))
def sell_(user,text):
	if text=="emerald":
		if values.Data[user]["items"]["emerald"]>99999:
			if values.Data[user]["items"].get("dxp")!=None:
				level_up_dxp(user)
				values.Data[user]["items"]["emerald"]=0
				lvv=values.Data[user]["items"]["level"]
				return(messg.emerald(user,lvv))
			else:
				return(messg.emeraldnodxp(user))
		else:
			return(messg.emeraldno(user))
def say_(user,text):
	if text.startswith("/execute") or text.startswith("/ignore") or text.startswith("/toggle"):
		return("ignored "+user)		
	return(text)
def help_(user,hhh):
	return(messg.newhelp)	
def load_(user,text):
	load_me()
	print("json loaded into object")
	return(None)
def want_(user,fff):
	return(messg.wanting(user,fff))
def gerald_(user,fff):
	return(random.choice((messg.gerald1,messg.gerald2,messg.gerald3,messg.gerald4,messg.gerald5,messg.gerald6,messg.gerald7)))
def command_(user,text):
	return(">>>CultGame1:mine,craft,sell,prestige,sacrifice,inv Others:say,want")


cmdlist_chat_whisper=(	#all the commands that result in the bot talking when talked, and whisper when whisper
	{"help":help_,"mine":mine_,"craft":craft_,"prestige":prestige_,"inv":inv_,
	"want":want_,"index":index_,"load":load_,"level":level_,"sell":sell_,
	"sacrifice":sacrifice_,"command":command_})
cmdlist_chat_chat={"say":say_,"gerald":gerald_} #all the commands that result in the bot talking, period
cmdlist_whisper_whisper={}
cmdlist_whisper_chat={}




