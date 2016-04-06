from IParser import IParser
from Transaction import Transaction
from parser.CyberMars.FieldFactory import FieldFactory
import logging
_logger = logging.getLogger(__name__)

CyberMarsFormat = {
    'SEQ': (1, 8),
    'TransactionType': (9, 9),
    'MerchantId': (10, 19),
    'CardNo': (20, 35),
    'ExpireDate': (36, 39),
    'TransactionAmount': (40, 51),
    'TransactionDate': (52, 59),
    'TransactionTime': (60, 65),
    'CardType': (66, 66)
}

class CyberMarsParser(IParser):
    def __init__(self):
        super(CyberMarsParser, self).__init__()

    def parse_file(self, file_path):
        _logger.info('start parse file')
        _trans_list = []
        with open(file_path, 'r') as fp:
            for line in fp.readlines():
                trans = self._parse_trans(line)
                _trans_list.append(trans)
        _logger.debug('trans list result: {}'.format(_trans_list))
        return _trans_list

    def _parse_trans(self, line):
        trans = Transaction()
        for field, pos in CyberMarsFormat.iteritems():
            _logger.debug('Field: {}, Pos: {}'.format(field, pos))
            if hasattr(trans, field):
                head = pos[0] - 1
                tail = pos[1]
                content = line[head:tail]
                _logger.debug('Origin Content: {}'.format(content))
                tmp_field = FieldFactory.get_field(field, content)
                _logger.debug('{}: {}'.format(field, tmp_field.get_value()))
                setattr(trans, field, tmp_field.get_value())
            else:
                raise Exception
            _logger.debug('===============================================')
        return trans