from parser.IField import IField

class TransactionTime(IField):
    def __init__(self, origin_value):
        super(TransactionTime, self).__init__(origin_value)
        self.value = TransactionTime.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return origin_value