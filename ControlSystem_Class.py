from config import pU
from p_Class import p
import random
class ControlSystem:

    def __init__(self):
        self.opponents = []
        self.team = []

    def clearString(self, string):
        cleaned_string = string.strip("(),'")
        return cleaned_string

    def updateEffects(self, entity):
        currenteffects = entity.applied_effects
        effectsToRemove = []
        for oneEffect in currenteffects:
            dur = oneEffect.duration
            if dur != 999:
                dur -= 1
                setattr(oneEffect, "duration", dur)
                if dur <= 0:
                    effectsToRemove.append(oneEffect)

            affected_attr = oneEffect.get_attribute()
            mode = oneEffect.get_effect()
            amount = oneEffect.get_value()
            effect_type = oneEffect.get_type()
            string_mode = str(mode)
            add_or_reduce = self.clearString(string_mode)


            if effect_type == 1:
                if add_or_reduce == "add":
                    entity.set_attribute(affected_attr, add_or_reduce, amount)
                elif add_or_reduce == "reduce":
                    entity.set_attribute(affected_attr, add_or_reduce, amount)
                else:
                    print("something went wrong")
            elif effect_type == 0:
                if add_or_reduce == "add":
                    entity.set_attribute(affected_attr, add_or_reduce, amount)
                    oneEffect.set_value(0)
                elif add_or_reduce == "reduce":
                    entity.set_attribute(affected_attr, add_or_reduce, amount)
                    oneEffect.set_value(0)
                else:
                    print("something went wrong")


        if len(effectsToRemove) > 0:
            for runouteffects in effectsToRemove:
                currenteffects.remove(runouteffects)



    def add_opponents(self, array_opp):
        if len(array_opp) <= 3:
            for item in array_opp:
                self.opponents.append(item)

    def add_team(self, array_team):
        if len(array_team) <= 3:
            for item in array_team:
                self.team.append(item)


    def createPEntity(self, name):
        p_archive = pU[name]
        if p_archive:
            name = p(p_archive["name"], p_archive["max_hp"], p_archive["current_hp"], p_archive["ap"], p_archive["defense"], p_archive["can_act"], 1)
            return name

    def createEEntity(self, name):
        e_archive = pU[name]
        if e_archive:
            name = p()


    def round_system(self):
        turn_count = 0
        side = 1

        while len(self.opponents) > 0 and len(self.team) > 0:
            turn_count += 1
            print("Turn ", turn_count)
            avail_atk = random.randint(0, 3)

            while avail_atk > 0:
                print("One attack")

            self.opponents.clear()









