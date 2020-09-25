

class Sword:
    """all swords by default have 100 uses"""
    def __init__(self):
        self.broken = False
        self.num_uses = 100

    def swing(self):
        # every swing, the number of uses left goes down by one
        # cannot swing a broken sword
        if self.broken:
            print("Go to the blacksmith! Cannot swing!")
            return
        self.num_uses -= 1
        print("Sword has been swung. Number of Uses Left: " + str(self.num_uses))
        if self.num_uses <= 0:
            self.broken = True
            print("Sword is broken!")
        return

    def repair(self):
        if self.broken:
            self.num_uses = 100
            self.broken = False
            print("Sword has been repaired!")
        return


class UnbreakableSword:
    """all swords by default have 100 uses, though this is a special sword, so after it reaches the number of swing limit then it disappears."""
    def __init__(self):
        self.disappear = False
        self.num_uses = 100

    def swing_unbreakable(self):
        if self.disappear:
            print("No longer exists")
            return
        self.num_uses -= 1
        print("Unbreakable sword has been swung! Number of Uses Left: " + str(self.num_uses))
        if self.num_uses <= 0:
            self.disappear = True
            print("The sword has disappeared!")
        return


class MasterSword(Sword):
    """only one master sword"""
    __instance = None

    def __init__(self):
        if MasterSword.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            MasterSword.__instance = self

        self.broken = False
        self.num_uses = 100

    @staticmethod
    def get_instance():
        if MasterSword.__instance is None:
            MasterSword()
        return MasterSword.__instance