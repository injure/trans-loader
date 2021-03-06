from parser.IField import IField

class TransactionDate(IField):
    def __init__(self, origin_value):
        super(TransactionDate, self).__init__(origin_value)
        self.value = TransactionDate.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return origin_value[:4] + '/' + origin_value[4:6] + '/' + origin_value[6:]