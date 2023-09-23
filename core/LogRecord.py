class LogRecord(object):
    def __init__(self, property_provider, writer):
        self.logger = property_provider('logger')
        self.level = property_provider('level')
        self.message = property_provider('message')
        self.time = property_provider('time')
        self.writer = writer
