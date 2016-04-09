from SEQ import SEQ
from TransactionType import TransactionType
from MerchantId import MerchantId
from CardNo import CardNo
from ExpireDate import ExpireDate
from TransactionAmount import TransactionAmount
from TransactionDate import TransactionDate
from TransactionTime import TransactionTime
from CardType import CardType

class FieldFactory(object):
    def __init__(self):
        pass

    @classmethod
    def get_field(cls, field_name, origin_value):
        if field_name == 'SEQ':
            return SEQ(origin_value)
        elif field_name == 'TransactionType':
            return TransactionType(origin_value)
        elif field_name == 'MerchantId':
            return MerchantId(origin_value)
        elif field_name == 'CardNo':
            return CardNo(origin_value)
        elif field_name == 'ExpireDate':
            return ExpireDate(origin_value)
        elif field_name == 'TransactionAmount':
            return TransactionAmount(origin_value)
        elif field_name == 'TransactionDate':
            return TransactionDate(origin_value)
        elif field_name == 'TransactionTime':
            return TransactionTime(origin_value)
        elif field_name == 'CardType':
            return CardType(origin_value)
        else:
            raise Exception









