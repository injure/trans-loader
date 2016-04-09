from IParser import IParser
from Transaction import Transaction
from parser.jsonfield.FieldFactory import FieldFactory
import json
import logging
_logger = logging.getLogger(__name__)

# field name of json file map to attribute name of object Transaction
JsonFormat = {
    'DataSeq': 'SEQ',
    'TransactionType': 'TransactionType',
    'MerchantId': 'MerchantId',
    'CardNo': 'CardNo',
    'ExpiredDate': 'ExpireDate',
    'TransactionAmount': 'TransactionAmount',
    'TransactionDate': 'TransactionDate',
    'TransactionTime': 'TransactionTime',
    'CardType': 'CardType'
}

class JsonParser(IParser):
    def __init__(self):
        super(JsonParser, self).__init__()

    def parse_file(self, file_path):
        _logger.info('start parse file')
        _trans_list = []
        with open(file_path, 'r') as file:
            json_list = json.load(file)
            _logger.debug('data in json file: {}'.format(json_list))
            for _dict in json_list:
                trans = self._parse_trans(_dict)
                _trans_list.append(trans)
        _logger.debug('trans list result: {}'.format(_trans_list))
        return _trans_list

    def _parse_trans(self, dict):
        _trans = Transaction()
        for key, value in dict.iteritems():
            field_name = JsonFormat[key]
            if hasattr(_trans, field_name):
                _tmp_field = FieldFactory.get_field(field_name, value)
                setattr(_trans, field_name, _tmp_field.get_value())
                _logger.debug('Field: {}'.format(field_name))
                _logger.debug('Origin Content: {}'.format(value))
                _logger.debug('{}: {}'.format(field_name, _tmp_field.get_value()))
            else:
                raise Exception
            _logger.debug('===============================================')
        return _trans

if __name__ == '__main__':
    parser = JsonParser()
    trans_list = parser.parse_file('../charge/test.json')
    for trans in trans_list:
        print trans.to_string()
