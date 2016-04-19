class IField(object):
    def __init__(self, origin_value):
        self.value = origin_value

    @classmethod
    def change_format(cls, origin_value):
        return origin_value

    def get_value(self):
        return self.value