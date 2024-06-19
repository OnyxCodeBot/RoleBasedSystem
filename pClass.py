

class p:
    def __init__(self, name, max_hp, current_hp, ap, defense, is_alive):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.ap = ap
        self.defense = defense
        self.is_alive = is_alive

    def get_name(self):
        return self.name

    def set_hp(self, action, amount):
        if action == 'add':
            self.current_hp += amount
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp

        if action == 'reduce':
            self.current_hp -= amount
            if self.current_hp <= 0:
                self.is_alive = 0
            else:
                self.is_alive = 0

