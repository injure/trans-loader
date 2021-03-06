from CyberMarsParser import CyberMarsParser
from CsvParser import CsvParser

class ParserFactory(object):
    def __init__(self):
        pass

    @classmethod
    def get_parser(cls, file_path):
        extension = file_path.split('.')[-1].lower()
        if extension == 'char':
            return CyberMarsParser()
        elif extension == 'csv':
            return CsvParser()
        else:
            raise Exception