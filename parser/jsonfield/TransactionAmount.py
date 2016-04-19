from decimal import Decimal

from parser.interface.IField import IField


class TransactionAmount(IField):
    def __init__(self, origin_value):
        super(TransactionAmount, self).__init__(origin_value)
        self.value = TransactionAmount.change_format(origin_value)

    @classmethod
    def change_format(cls, origin_value):
        return Decimal(origin_value)