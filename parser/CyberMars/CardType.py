from parser.interface.IField import IField
class CardType(IField):

    transform = {
        '3': 'CardType.UnionPay',
        '2': 'CardType.MASTER',
        '1': 'CardType.VISA',
        '0': 'CardType.JCB'
    }

    def __init__(self, origin_value):
        super(CardType, self).__init__(origin_value)
        self.value = CardType.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return CardType.transform.get(origin_value)
