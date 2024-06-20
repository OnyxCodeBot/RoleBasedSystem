
class ControlSystem:
    turn = 0


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

