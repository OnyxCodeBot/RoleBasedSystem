
class ControlSystem:
    turn = 0

    def updateEffects(self, entity):
        currenteffects = entity.applied_effects
        effectsToRemove = []
        for effect in currenteffects:
            dur = effect.duration
            if dur != 999:
                dur -= 1
                setattr(effect, "duration", dur)
                if dur <= 0:
                    effectsToRemove.append(effect)

            print(effect.get_effect())
            affected = effect.attribute
            mode = effect.get_effect()
            amount = effect.value


            if hasattr(entity, str(affected)):
                print(str(mode))
                if str(mode) == "add":
                    oldvalue = getattr(entity, str(affected))
                    print(oldvalue)
                    oldvalue += amount
                    setattr(entity, str(affected), amount)
                elif str(mode) == "reduce":
                    oldvalue = getattr(entity, str(affected))
                    print(oldvalue)
                    oldvalue += amount
                    setattr(entity, str(affected), amount)
                else:
                    print("something went wrong")

        if len(effectsToRemove) > 0:
            for runouteffects in effectsToRemove:
                currenteffects.remove(runouteffects)

