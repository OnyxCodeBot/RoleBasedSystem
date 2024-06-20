
class StatusE:
    def __init__(self, name, attribute, effect, value, duration, type, can_be_cleared):
        self.name = name
        self.attribute = attribute
        self.effect = effect,
        self.value = value
        self.duration = duration
        self.type = type
        self.can_be_cleared = can_be_cleared

    def get_name(self):
        return self.name

    def get_attribute(self):
        return self.attribute

    def get_effect(self):
        return self.effect

    def get_value(self):
        return self.value

    def set_value(self, newval):
        setattr(self, "value", newval)

    def get_duration(self):
        return self.duration

    def get_type(self):
        return self.type


