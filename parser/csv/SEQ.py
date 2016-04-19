from parser.interface.IField import IField

class SEQ(IField):
    def __init__(self, origin_value):
        super(SEQ, self).__init__(origin_value)
        self.value = SEQ.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return origin_value