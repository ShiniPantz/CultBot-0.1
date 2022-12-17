spam1="grind, win, earn in the next CultSeason!"
spam2="Join the Cult, discord invite code yvyUuaeeUK"
spam3="don't type <C_help> in chat"
spam4='make me say anything with "C_say [message]"'
spam5="no u"
spam6="pls report bugs if you find them"
spam7="shoutouts to GeraldBot"


gerald1=">gerald >CultBot sucks, GeraldBot on top"
gerald2=">gerald >Python is trash"
gerald3=">gerald >I live rent free in your head"
gerald4=">gerald >I am clearly the better coder"
gerald5=">gerald >you never touched ass?"
gerald6=">gerald >nn dog"
gerald7=">gerald >nice iq monkey"
def logpublic(user,message):
	return(f'{user} said "{message}"')
def logprivate(user,message):
	return(f'{user} whispered "{message}"')
brokenlol=">>>The bot is broken lol"


index_='>>>learn about items with ">C_index [itemname]" for example >C_index diamond'
index_diamond=">>>mined with >C_mine, used to craft bloccs and gives xp when >C_craft is used"
index_blocc=">>>multiplies >C_mine efficiency, generate [1*level] prusing [9*level] diamonds with >C_craft"
index_xp=">>>generated after >C_craft (xp=(diamond-9*blocc)*matter*-antimatter), level up every level*100xp"
index_level=">>>multiplies >C_craft efficiency"
index_matter=">>>multiplies xp gain, after prestige is SET to previous_level-antimatter"
index_antimatter=">>>multiplies xp gain, after prestige is ADDED to current antimatter value"



def prestige1(levv):
	return(f">>>you can create between 5 and {levv} antimatter, no more")
prestige2=">>>you need at least 5 levels to create antimatter"
def prestige3(user,matter,amatter):
	return(f">>>{user} wiped his inventory for {matter} matter and {amatter} antimatter")
prestige4=">>>pls give me a number"



help_='>>> >C_help [want][game][inv][mine][craft][say][index][prestige]'
help_want=r'>>>bot.chat(f">>>{user} want'+r"'s to {fff}"+'")'
help_game='>>>do >C_game [number], try to reach "zero" :)'
help_inv=">>>shows your inventory"
help_mine=">>>mine 1-5 diamonds, multiplied by blocc"
help_craft=">>>use diamonds to craft blocc"
help_say=">>>make me say anything, including /commands (/w only works when the server feels like it)"
help_index='>>>learn about items with ">C_index [itemname]" for example >C_index diamond'
help_prestige='>>>resets the game, given ">C_prestige [number], while level>number>5, ADDS number*(-1)+=antimatter and SETS number-antimatter=matter'


def wanting(user,fff):
	return(f">>>{user} want's to {fff}")



savedd=">>>game saved"


def getinv(user,level,xp,balance,blocc):
	return(f">>>{user} has {balance} diamonds, {blocc} blocc's")
def getinv2(user,matter,amatter):
	return(f">>>{user} has {matter} matter and {amatter} antimatter, giving a {-matter*amatter}x bonus to xp gain")
def mininh(user,mined,btype):
	return(f">>>{user} just mined {mined} {btype}s")
def craff(user,lvv,dia,x1,x2,cost,rxturn,text):
	return(f">>>{user} just crafted {lvv*rxturn} {text}_blocc and get's {(dia-(cost*lvv))*x1*x2*-1}xp")
def craff0(user,lvv,cost,rxturn,text):
	return(f">>>{user} you are poor, try C_mine to get rich. You need {cost*lvv} diamonds for {lvv*rxturn} {text}_blocc")
def cccld(cooldown):
	return(f">>>cooldown says {cooldown}")
def dlvv(user,dxp,lvv,mx):
	return(f">>>{user} has {dxp}dxp, decaying at a rate of {lvv*mx}/second")
def levelss(user,lvv,xp,exp):
	return(f">>>{user} is lv{lvv} with {xp}/{int(100*lvv+(exp**lvv))}xp ({int(100*xp/(100*lvv+(exp**lvv)))}%)")




sacno=">>>you need 100 levels to sacrifice, check C_level"
def sac1st(user):
	return(f">>>{user} you completed the first chapter and earned 1 XP_bottle. hooray. create a black hole for chapter 2")
def sac(user, bottle):
	return(f">>>{user} sacrificed his life for another XP_bootle, and has a total of {bottle}")
def xinv_singleblcc(user,amount,typè):
	return(f">>>{user} has {amount} {typè}_blocc")
def xinv_blcc(user,add,multiply):
	return(f">>>{user} has {add}bloccs, giving a {multiply}x bonus to mining")
def xinv(user,amount,typè):
	return(f">>>{user} has {amount} {typè}")
def xinv_fail(user,text):
	return(f">>>{user} you don't own any {text}")
def xinv_prestige(user,bonus,matter,amatter):
	return(f">>>{user} has {matter} matter and {amatter} antimatter, giving a {bonus}x bonus to xp gain")

def emerald(user,lvv):
	return(f">>>{user} used his emeralds and dxp to reach level {lvv}")
def emeraldnodxp(user):
	return(f">>>{user} you don't have any dxp")
def emeraldno(user):
	return(f">>>{user} you need at least 100000 emerald")

newhelp=">>>join my server with the invite code yvyUuaeeUK and go to #CultBot_help, or do C_commands"







