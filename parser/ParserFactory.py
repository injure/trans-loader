from CyberMarsParser import CyberMarsParser
class ParserFactory(object):
    def __init__(self):
        pass

    @classmethod
    def get_parser(cls, file_path):
        extension = file_path.split('.')[-1].lower()
        if extension == 'char':
            return CyberMarsParser()
        elif extension == 'cvs':
            raise NotImplementedError
        else:
            raise Exception