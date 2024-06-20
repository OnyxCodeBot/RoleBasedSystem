from config import effects
from SE_Class import StatusE

class p:
    def __init__(self, name, max_hp, current_hp, ap, defense, can_act, is_alive):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.ap = ap
        self.defense = defense
        self.can_act = can_act
        self.applied_effects = []
        self.is_alive = is_alive

    def get_name(self):
        return self.name


    def get_attr(self):
        print("--- ", self.name, " ---")
        print("HP: ", self.current_hp)
        print("AP: ", self.ap)
        print("Def: ", self.defense)
        print(" ")


    def check_if_eliminated(self):
        if self.current_hp <= 0:
            self.is_alive = 0
            return 0
        else:
            self.is_alive = 1
            return 1

    def check_if_over_max_hp(self):
        if self.current_hp > self.max_hp:
            self.max_hp = self.current_hp

    def set_attribute(self, attr, action, amount): # needs "self.some_attr" for attr
        if hasattr(self, attr):
            if action == 'add':
                attribut_value = getattr(self, attr)
                attribut_value += amount
                setattr(self, attr, attribut_value)
                self.check_if_over_max_hp()

            elif action == 'reduce':
                attribut_value = getattr(self, attr)
                attribut_value -= amount
                setattr(self, attr, attribut_value)
                # print("Set ", attr, " to ", attribut_value)
                self.check_if_eliminated()
            else:
                print("something went wrong")

    def kill_p(self):
        self.is_alive = 0


    def engageOtherEntity(self, selectedE):
        return selectedE

    def debufEntity(self, debuff, enemyentity):
        configSE = effects[debuff]

        e_name = configSE['shown_name']
        e_attr = configSE["affected_attribute"]
        e_eff = configSE["effect"]
        e_value = configSE["value"]
        e_duration = configSE['duration']
        e_type = configSE["type"]
        e_clearable = configSE["can_be_cleared"]
        giveDebuff = StatusE(e_name, e_attr, e_eff, e_value, e_duration, e_type, e_clearable)
        # print(e_name, e_attr, e_eff, e_value)
        enemyentity.applied_effects.append(giveDebuff)

    def show_own_debuffs(self):
        print("Current Effects: ")
        if len(self.applied_effects) > 0:
            for debuff in self.applied_effects:
                if debuff.duration != 999:
                    print(debuff.name, " ", debuff.duration, "Turns left")
                else:
                    print(debuff.name)
        else:
            print("No Effects")
