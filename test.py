import importlib
import pkgutil

class dynamic_import(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    # module = importlib.import_module('parser.CsvParser')
    # print module
    # my_class = getattr(module, 'CsvParser')
    # print my_class
    # instance = my_class()

    for n in pkgutil.iter_modules(['parser'], 'prefix.'):
        print n