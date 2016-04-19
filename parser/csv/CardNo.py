from parser.interface.IField import IField

class CardNo(IField):
    def __init__(self, origin_value):
        super(CardNo, self).__init__(origin_value)
        self.value = CardNo.change_format(origin_value)