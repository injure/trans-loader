import logging

from ParserFactory import ParserFactory

_logger = logging.getLogger(__name__)

class TransLoader(object):
    def __init__(self):
        self._parser = None

    def load_charge_file(self, file_path):
        _logger.info('start load charge file')
        self._prepare_parser(file_path)
        _trans_list = self._parse_file(file_path)
        return _trans_list

    def _prepare_parser(self, file_path):
        self._parser = ParserFactory.get_parser(file_path)
        _logger.debug('get {}'.format(type(self._parser)))


    def _parse_file(self, file_path):
        return self._parser.parse_file(file_path)