class IParser(object):
    def __init__(self, extension):
        self.extension = extension

    def parse_file(self, file_path):
        raise NotImplementedError