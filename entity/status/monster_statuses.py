import base

class OgreEnrage(base.Entity):
    def __init__(self):
        super(OgreEnrage,self).__init__()
        self.turns = 0
        self.applied = False

    def do_turn(self,option):
        if self.turns < 3:
            if not self.applied:
                self.owner.power *= 1.2
                self.owner.health *= 1.2
                self.applied = True
            self.turns += 1
        else:
            self.owner.power /=1.2
            self.owner.statuses.remove(self)
