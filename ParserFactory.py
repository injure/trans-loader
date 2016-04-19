import pkgutil
import importlib

class ParserFactory(object):
    def __init__(self):
        pass

    @classmethod
    def get_parser(cls, file_path):
        extension = file_path.split('.')[-1].lower()
        mod_name_list = [mod_name for _, mod_name, pkg in pkgutil.iter_modules(['parser']) if pkg is False]
        for mod_name in mod_name_list:
            module = importlib.import_module('parser.' + mod_name)
            parser_class = getattr(module, mod_name)
            parser = parser_class()
            if parser.extension == extension:
                return parser
        raise Exception

if __name__ == '__main__':
    ParserFactory.get_parser('test.csv')