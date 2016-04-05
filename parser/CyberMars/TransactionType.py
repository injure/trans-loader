from parser.IField import IField

class TransactionType(IField):

    transform = {
        '0': 'TransType.SALE',
        '1': 'TransType.Refund'
    }

    def __init__(self, origin_value):
        super(TransactionType, self).__init__(origin_value)
        self.value = TransactionType.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return TransactionType.transform.get(origin_value)