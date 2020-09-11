import json

# Internal log record - sinks produces this objects
class LogRecord(object):
    def __init__(self, logger, level, message, time):
        self.logger = logger
        self.level = level
        self.message = message
        self.time = time

    def asString(self):
        return "{}|{}|{}|{}".format(self.time, self.level, self.logger, self.message)
    
   
    @classmethod
    def fromJson(cls, jsonText):
        js = json.loads(jsonText)
        return LogRecord(js['logger'], js['level'], js['message'], js['time'])
