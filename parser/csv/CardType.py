from parser.interface.IField import IField
class CardType(IField):

    transform = {
        'U': 'CardType.UnionPay',
        'M': 'CardType.MASTER',
        'V': 'CardType.VISA',
        'J': 'CardType.JCB'
    }

    def __init__(self, origin_value):
        super(CardType, self).__init__(origin_value)
        self.value = CardType.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return CardType.transform.get(origin_value)
