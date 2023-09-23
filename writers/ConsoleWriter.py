from core.Config import Config
from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord
from termcolor import cprint
import os

class ConsoleWriter(AbstractWriter):
    def __init__(self, name):
        self.name = name
        os.system('color')

    def logLevel2Color(self, level):
        if level in Config.level_defs():
            return Config.level_defs()[level]
        return "green"        

    def write_record(self, lr: LogRecord):
        cprint(self.format_console(lr), self.logLevel2Color(lr.level))

    def format_console(self, lr: LogRecord):
        return f"{lr.time}|{lr.level}|{lr.logger}|{lr.message}"