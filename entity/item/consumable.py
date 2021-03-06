import entity.item.items
import entity.status.player_statuses as s
import base
# this extends item but overrides return_options to allow it to return an option
# if it isnt equipped

class HealthPotion(entity.item.items.ItemUsedFromInventory):
	def __init__(self):
		super(HealthPotion,self).__init__()
		##self.options = ['drink health potion']
		self.name = 'health potion'
		self.cost = 20
	def do_turn(self,option):
		pass
		# the player can only have one health potion active at a time
		##if option == self.options[0] and not self.owner.statuses.contains_type(s.Healing):
		##	base.put("%s consumes a health potion!" % self.owner.name)
		##	self.owner.statuses.append(s.Healing())
		##	self.owner.inventory.remove(self)
	def add_to_inventory(self):
		for a in self.owner.inventory:
			if isinstance(a,HealthSack):
				a.add()
		self.owner.inventory.remove(self)

class Sack(entity.item.items.ItemUsedFromInventory):
	def __init__(self,contents):
		super(Sack,self).__init__()
		self.contents = contents
		self.options = ['open sack']
		self.name = 'a rugged sack'

	def do_turn(self,option):
		if option == 'open sack':
			de = ''
			for a in self.contents:
				self.owner.inventory.append(a)
				de += '%s, ' % a.name
			base.put('you open the sack and find %s' % de[:-2])
			self.owner.inventory.remove(self)

class HealthSack(entity.item.items.ItemUsedFromInventory):
	def __init__(self):
		super(HealthSack,self).__init__()
		self.contents =0
		self.options= []
		self.name = 'a bag of health'

	def add(self):
		self.contents+=1
		self.options = ['drink a health potion (x%d)' % self.contents]

	def do_turn(self,options):
		try:
			if options == self.options[0] and self.contents>0:
				self.owner.statuses.append(s.Healing())
				self.contents-=1
				if self.contents != 0:
					self.options = ['drink a health potion (x%d)' % self.contents]
				else:
					self.options = []
		except:
			pass
