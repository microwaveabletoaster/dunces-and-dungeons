import base, random, time

class Apply(object):
	def __init__(self):
		pass
	def modify_monster(self,Monster):
		Mod={"Acidic":{"health":"*.5","power":"+10"},
	 	"Camphoric":{"health":"*.5", "power":"*2","ap":"+1"},
	 	"Caustic":{"health":"*.5"},
	 	"Dank":{"health":"*1.5","power":"*2","ap":"+2"},
	 	"Decaying":{"health":"*.3","power":"+-40","ap":"+-1"},
	 	"Destructive":{"health":"*1.2","power":"+90"},
	 	"Dieing":{"health":"*.05","power":"/20"},
	 	"Dusty":{"health":"*.7","power":"/2"},
	 	"Fetid":{"health":"*.2","power":"/2"},
		"Flowery":{"health":"=1","power":"=1","level":"=1","ap":"=1","baseap":"=1"},
		"Forgotten":{"health":"1.1","power":"/2"},
		"Foul":{"health":"*.8","power":"+-12"},
		"Funky":{"health":random.choice('+=')+str(random.randint(1,1000)),"power":random.choice('+*=')+str(random.randint(1,100)),"level":random.choice('+=')+str(random.randint(1,10)),"ap":random.choice('+*=')+str(random.randint(1,2))},
		"Lightning":{"health":"*.1","power":"*3","ap":"*2"},
		"Lowly":{"health":"*.4","power":"/2","ap":"=1"},
		"Musky":{"health":"*2","power":"*2","ap":"+2"},
		"Nasty":{"health":"*.9","power":"+20"},
		"Normal":{},
		"Putrid":{"health":"*.6","power":"/10"},
		"Rancid":{"health":"+-20","power":"+-5"},
		"Scorched":{"health":"*.4","power":"/2"},
		"Tiny":{"health":"*.3","power":"/3"},
		"Weak":{"health":"*.1","power":"/5"}}
		run=Mod[random.choice(Mod.keys())]

		for a in run:
			if(a=="health"):
				if(run[a][0]=="+"):
					Monster.health=Monster.health+float(run[a][1:len(run[a])])
				elif(run[a][0]=="*"):
					Monster.health=Monster.health*float(run[a][1:len(run[a])])
				elif(run[a][0]=="="):
					Monster.health=float(run[a][1:len(run[a])])
				elif(run[a][0]=="/"):
					Monster.health=Monster.health/int(run[a][1:len(run[a])])
			elif(a=="power"):
				if(run[a][0]=="+"):
					Monster.power=Monster.power+int(run[a][1:len(run[a])])
				elif(run[a][0]=="*"):
					Monster.power=Monster.power*(run[a][1:len(run[a])])
				elif(run[a][0]=="="):
					Monster.power=int(run[a][1:len(run[a])])
				elif(run[a][0]=="/"):
					Monster.power=Monster.power/int(run[a][1:len(run[a])])
			elif(a=="level"):
				if(run[a][0]=="+"):
					Monster.level=Monster.level+int(run[a][1:len(run[a])])
				elif(run[a][0]=="*"):
					Monster.level=Monster.level*int(run[a][1:len(run[a])])
				elif(run[a][0]=="="):
					Monster.level=int(run[a][1:len(run[a])])
				elif(run[a][0]=="/"):
					Monster.level=Monster.level/int(run[a][1:len(run[a])])
			elif(a=="ap"):
				if(run[a][0]=="+"):
					Monster.action_points=Monster.action_points+int(run[a][1:len(run[a])])
				elif(run[a][0]=="*"):
					Monster.action_points=Monster.action_points*int(run[a][1:len(run[a])])
				elif(run[a][0]=="="):
					Monster.action_points=int(run[a][1:len(run[a])])
				elif(run[a][0]=="/"):
					Monster.action_points=Monster.action_points/int(run[a][1:len(run[a])])
			elif(a=="baseap"):
				if(run[a][0]=="+"):
					Monster.base_ap=Monster.base_ap+int(run[a][1:len(run[a])])
				elif(run[a][0]=="*"):
					Monster.base_ap=Monster.base_ap*int(run[a][1:len(run[a])])
				elif(run[a][0]=="="):
					Monster.base_ap=int(run[a][1:len(run[a])])
				elif(run[a][0]=="/"):
					Monster.baseap=Monster.baseap/int(run[a][1:len(run[a])])
		Monster.name=namer+" "+ Monster.name
		return Monster



class Monster(base.Entity):
	def __init__(self,level):
		super(Monster,self).__init__()
		self.name="Monster"
		self.aggro = None
		self.aggroed = False
		self.probablity = 0.0

		self.health = 100
		self.level=1
		self.power=self.level*10
		self.multiplier=1
		# base ap is what the ap should be restored to after a turn is complete
		self.base_ap = 3
		self.alive = True
		self.action_points = 3
		self.options = []
		self.inventory = base.Inventory(self)
		self.statuses = base.Inventory(self)
		self.owner = None


	def set_level(self,val):
		pass

	def do_turn(self):
		for a in self.statuses:
			a.do_turn()

		if self.action_points > 0:
			if not self.aggroed:
				self.aggro = random.choice(self.owner.party.inventory)
			self.aggroed = True
					
			self.attack(self.aggro)

	def attack(self,target):
		self.reveal()
		target.take_damage(self,self.power)

	def to_str(self):
		return self.name

	def examine(self,examiner):
		return self.to_str()
		self.reveal()

	def reveal(self):
		self.owner.things.remove(self)
		self.owner.identified_things.append(self)
		
	def dev_examine(self):
		print 'name: %s health: %d, attributes: %s, power: %s, level: %d' % (self.name, self.health,str(self.attributes),self.power,self.level)

	def kill(self):
		self.alive = False
		self.owner.things = self.owner.things[:self.owner.things.index(self)]+self.owner.things[self.owner.things.index(self)+1:]

# def compute(comp,val):
	


def spawn(level):
	app=Apply()
	ret = []
	compound = []
	for key, val in MONSTERLIST.iteritems():
		if random.random() * 100 < val['probability']:
			compound
			for x in range(random.choice(range(val['groupsize']))+1):
				ret.append(app.modify_monster(key(level)))
	return ret

class Skeleton(Monster):
	def __init__(self,level):
		super(Skeleton,self).__init__(level)
		self.health=50+self.level*20
		self.power=10+self.level*10
		self.name="Skeleton"

	def to_str(self):
		return self.name

class Goblin(Monster):
	def __init__(self,level):
		super(Goblin,self).__init__(level)
		self.health=20+self.level*4
		self.multiplier=.5
		self.power=self.level*4
		self.name="Goblin"

## Hmmmmm..... My spiders health change has disappearrf
class Spider(Monster):
	def __init__(self,level):
		super(Spider,self).__init__(level)
		self.multiplier=.4
		self.power=2+self.level*1
		self.name="Spider"

class Assassin(Monster):
	def __init__(self,level):
		super(Assassin,self).__init__(level)
		self.health=1+self.level*5
		self.multiplier=1.5
		self.power=20+self.level*25
		self.name="Assassin"

class Hidden_Devourer(Monster):
	def __init__(self,level):
		super(Hidden_Devourer,self).__init__(level)
		self.health=5+self.level*3
		self.multiplier=.6
		self.power=20+self.level*30
		self.ap=1
		self.action_points=1
		self.name="Hidden Devourer"


class Ogre(Monster):
	def __init__(self,level):
		super(Ogre,self).__init__(level)
		self.health=200*self.level*40
		self.power=5+self.level*1;
		self.name="Ogre"

class Hellhound(Monster):
	def __init__(self,level):
		super(Hellhound,self).__init__(level)
		self.health=100+self.level*25
		self.multiplier=1.1
		self.power=15+self.level*12
		self.name="Hellhound"

class Sorcerer(Monster):
	def __init__(self,level):
		super(Sorcerer,self).__init__(level)
		self.health=75+self.level*10
		self.multiplier = .9
		self.power=25+self.level*10
		self.name="Sorcerer"

class Elemental(Monster):
	def __init__(self,level):
		super(Elemental,self).__init__(level)
		self.health=60+self.level*20
		self.power=20+self.level*7
		self.name="Elemental"
class Meme(Monster):
	def __init__(self,level):
		super(Meme,self).__init__(level)
		self.health=420+self.level*9.11
		self.power=69+self.level*42
		self.name ="Meme"
class WindElemental(Elemental):
	def __init__(self,level):
		super(WindElemental,self).__init__(level)
		self.health=40+self.level*10
		self.power=10+self.level*9
		self.name="Wind Elemental"

class WaterElemental(Elemental):
	def __init__(self,level):
		super(WaterElemental,self).__init__(level)
		self.power=15+self.level*10
		self.name="Water Elemental"

class FireElemental(Elemental):
	def __init__(self,level):
		super(FireElemental,self).__init__(level)
		self.health=30+self.level*12
		self.power=30+self.level*12
		self.name="Fire Elemental"

# here down are not added to the spawn list

class EarthElemental(Elemental):
	def __init__(self,level):
		super(EarthElemental,self).__init__(level)
		self.health=100+self.level*20
		self.power=15+self.level*8
		self.name="Earth Elemental"

class Demigod(Monster):
	def __init__(self,level):
		super(Demigod,self).__init__(level)
		self.multiplier=1.6
		self.health=200+self.level*18
		self.power=25+self.level*14
		self.action_points=2
		self.name="Demigod"

class Overcharger(Monster):
	def __init__(self,level):
		super(Overcharger,self).__init__(level)
		self.multiplier=1.05
		self.health=80+self.level*10
		self.power=50+self.level*30
		self.ap=1
		self.action_points=1
		self.name="Overcharger"

class Cyclops(Monster):
	def __init__(self,level):
		super(Cyclops,self).__init__(level)
		self.health=80+self.level*20
		self.power=20+self.level*10
		self.name="Cyclops"


MONSTERLIST = {
	Skeleton:{
		'probability':50.0,
		'groupsize':3
	},
	Goblin:{
		'probability':32.0,
		'groupsize':4
	},
	Spider:{
		'probability':40.0,
		'groupsize':8
	},
	Assassin:{
		'probability':12.0,
		'groupsize':2
	},
	Hidden_Devourer:{
		'probability':8.0,
		'groupsize':1
	},
	Ogre:{
		'probability':32.0,
		'groupsize':1
	},
	Hellhound:{
		'probability':32.0,
		'groupsize':4
	},
	Meme:{
		'probability':1.0,
		'groupsize':69 # fucking lol
	},
	WindElemental:{
		'probability':32.0,
		'groupsize':4
	},
	FireElemental:{
		'probability':32.0,
		'groupsize':4
	}
}
