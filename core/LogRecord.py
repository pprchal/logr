class LogRecord(object):
    def __init__(self, logger, level, message, time, writer):
        self.logger = logger
        self.level = level
        self.message = message
        self.time = time
        self.writer = writer
