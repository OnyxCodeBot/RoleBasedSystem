
class StatusE:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def applyEffect(self, entity):
        entity.applied_effects.append(self)
