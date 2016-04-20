from ConfigParser import RawConfigParser
import importlib

class ParserFactory(object):
    def __init__(self):
        pass

    @classmethod
    def get_parser(cls, file_path):
        extension = file_path.split('.')[-1].lower()
        cfg_parser = RawConfigParser()
        cfg_parser.read('config.ini')
        config_dict = dict(cfg_parser.items('parser'))
        if extension in config_dict:
            tar_parser_clsname = config_dict[extension]
        else:
            raise Exception
        module = importlib.import_module('parser.' + tar_parser_clsname)
        parser = getattr(module, tar_parser_clsname)
        return parser()

if __name__ == '__main__':
    parser = ParserFactory.get_parser('test.char')
    print type(parser)
    parser = ParserFactory.get_parser('test.csv')
    print type(parser)
    parser = ParserFactory.get_parser('test.json')
    print type(parser)
