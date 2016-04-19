from parser.interface.IField import IField

class ExpireDate(IField):
    def __init__(self, origin_value):
        super(ExpireDate, self).__init__(origin_value)
        self.value = ExpireDate.change_format(origin_value)