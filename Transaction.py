class Transaction(object):
    def __init__(self):
        self.SEQ = None
        self.TransactionType = None
        self.MerchantId = None
        self.CardNo = None
        self.ExpireDate = None
        self.TransactionAmount = None
        self.TransactionDate = None
        self.TransactionTime = None
        self.CardType = None

    def to_string(self):
        return str(self.SEQ) + ' ' + str(self.TransactionType) + ' ' + str(self.MerchantId) + ' ' + str(self.CardNo) + ' ' + \
               str(self.ExpireDate) + ' ' + str(self.TransactionAmount) + ' ' + str(self.TransactionDate) + ' ' + \
               str(self.TransactionTime) + ' ' + str(self.CardType)