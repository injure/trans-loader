from parser.interface.IField import IField

class MerchantId(IField):
    def __init__(self, origin_value):
        super(MerchantId, self).__init__(origin_value)
        self.value = MerchantId.change_format(origin_value)