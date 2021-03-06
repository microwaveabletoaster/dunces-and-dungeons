import entity.item.items
import base,random,math


# this is basically to identify what is armor and what isn't
class Armor(entity.item.items.Item):
	def __init__(self):
		super(Armor,self).__init__()
	def get_cost(self):
		return self.cost

	def register_damage(self,attacker,damage):
		for a in self.modifiers:
			a.do_turn(attacker,damage)

	def equip(self):
		super(Armor,self).equip()
		self.apply()
		self.name += '*'

	def unequip(self):
		super(Armor,self).unequip()
		self.exit()
		self.name = self.name[:-1]

class Shield(Armor):
	def __init__(self,level):
		super(Shield,self).__init__()
		self.name = 'shield'
		self.info='one-handed'
		self.equipable=True
		self.info2='nope'
		self.level = level
		self.cost=10.0
		self.item_options=['examine','equip']
		self.options=['%s' % self.to_str()]
		self.armor=12*self.level
		self.defendin=False
		self.blockin=False

	#I am not sure how to do the do_turn method.
	def do_turn(self,option):
		self.armor=12*self.owner.level
		self.options = ['%s' % self.to_str()]
		if self.defendin:
			for a in self.owner.party.inventory:
				a.armor-=(self.level*2)
			self.defendin=False
		if self.blockin:
			self.owner.armor-=(3*self.level)
			self.blockin=False
		if option == self.options[0]:
			p = base.make_choice(['Block with %s' % self.to_str(),'Defend Allies with %s' % self.to_str()])
			if p == 0:
				self.block()
			if p == 1:
				self.defend()
	#Imagining Blocking will increase armor by a set amount on top of the amount given passively from a shield and cost 1 action point
	#while Defending Allies will increase armor of all Allies (including you) by a set amount and cost 2 action points.

	def block(self):
		self.owner.armor+=(3*self.level)
		self.blockin=True

	def defend(self):
		for a in self.owner.party.inventory:
			a.armor+=(2*self.level)
		self.defendin=True
	def apply(self):
		self.owner.armor += self.armor

	def exit(self):
		self.owner.armor -= self.armor



class Breastplate(Armor):
	def __init__(self,level):
		super(Breastplate,self).__init__()
		self.name = 'breastplate'
		self.info='chest'
		self.equipable=True
		self.item_options=['examine','equip']
		self.level = level
		self.cost=15.0
		self.armor=20*level
	def register_damage(self,attacker,damage):
		self.armor=20*self.owner.level
		for a in self.modifiers:
			a.do_turn(attacker,damage)
				
	def apply(self):
		self.owner.armor += self.armor

	def exit(self):
		self.owner.armor -= self.armor


class Chainmail(Armor):
	def __init__(self,level):
		super(Chainmail,self).__init__()
		self.name = 'chainmail'
		self.item_options=['examine','equip']
		self.info='chest'
		self.equipable=True
		self.level = level
		self.cost=12.0
		self.armor=15*level

	def register_damage(self,attacker,damage):
		self.armor=15*self.owner.level
		for a in self.modifiers:
			a.do_turn(attacker,damage)

	def apply(self):
		self.owner.armor += self.armor

	def exit(self):
		self.owner.armor -= self.armor


class Platelegs(Armor):
	def __init__(self,level):
		super(Platelegs,self).__init__()
		self.name = 'platelegs'
		self.item_options=['examine','equip']
		self.info='legs'
		self.level = level
		self.equipable=True
		self.cost=10.0
		self.armor=12*level

	def register_damage(self,attacker,damage):
		self.armor=12*self.owner.level
		for a in self.modifiers:
			a.do_turn(attacker,damage)

	def apply(self):
		self.owner.armor += self.armor

	def exit(self):
		self.owner.armor -= self.armor


class Helmet(Armor):
	def __init__(self,level):
		super(Helmet,self).__init__()
		self.name = 'helmet'
		self.info='helmet'
		self.item_options=['examine','equip']
		self.level = level
		self.equipable=True
		self.cost=8.0
		self.armor=13*level

	def register_damage(self,attacker,damage):
		self.armor=13*self.owner.level
		for a in self.modifiers:
			a.do_turn(attacker,damage)

	def apply(self):
		self.owner.armor += self.armor

	def exit(self):
		self.owner.armor -= self.armor
