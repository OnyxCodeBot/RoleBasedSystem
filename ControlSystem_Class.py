
class ControlSystem:
    turn = 0

    def updateEffects(self, entity):
        currenteffects = entity.applied_effects
        effectsToRemove = []
        for effect in currenteffects:
            dur = effect.duration
            dur -= 1
            if dur <= 0:
                effectsToRemove.append(effect)
            else:
                print(effect, " has ", dur, " Turns left")

        for runouteffects in effectsToRemove:
            currenteffects.remove(runouteffects)

