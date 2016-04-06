from IParser import IParser
from Transaction import Transaction
from parser.csv.FieldFactory import FieldFactory
import logging
_logger = logging.getLogger(__name__)

CsvFormat = {
    'DATA_SEQ': 'SEQ',
    'TRANS_TYPE': 'TransactionType',
    'MERCHANT_ID': 'MerchantId',
    'CARD_NO': 'CardNo',
    'EXPIRED_DATE': 'ExpireDate',
    'TRANS_AMT': 'TransactionAmount',
    'TRANS_DATE': 'TransactionDate',
    'TRANS_TIME': 'TransactionTime',
    'CARD_TYPE': 'CardType'
}

class CsvParser(IParser):
    def __init__(self):
        super(CsvParser, self).__init__()

    def parse_file(self, file_path):
        _logger.info('start parse file')
        _trans_list = []
        with open(file_path, 'r') as file:
            _field_list = file.readline().strip('\n').split(',')
            _logger.debug('fields in csv file: {}'.format(_field_list))
            for line in file.readlines():
                trans = self._parse_trans(_field_list, line)
                _trans_list.append(trans)
        _logger.debug('trans list result: {}'.format(_trans_list))
        return _trans_list

    def _parse_trans(self, field_list, line):
        _content_list = line.strip('\n').split(',')
        _trans = Transaction()
        for i in range(len(field_list)):
            module_name = CsvFormat.get(field_list[i])
            if hasattr(_trans, module_name):
                _logger.debug('Field: {}'.format(module_name))
                tmp_field = FieldFactory.get_field(module_name, _content_list[i])
                _logger.debug('Origin Content: {}'.format(_content_list[i]))
                _logger.debug('{}: {}'.format(field_list[i], tmp_field.get_value()))
                setattr(_trans, module_name, tmp_field.get_value())
            else:
                raise Exception
            _logger.debug('===============================================')
        return _trans