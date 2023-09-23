from core.Config import Config
from core.Formatter import Formatter
from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord
from termcolor import cprint
import os


class ConsoleWriter(AbstractWriter):
    def __init__(self, name):
        super().__init__(name)
        os.system('color')

    @staticmethod
    def log_level_2color(level):
        """
        Translate log level to color
        :param level:
        :return:
        """
        if level in Config.level_defs():
            return Config.level_defs()[level]
        return "green"        

    async def write_record(self, lr: LogRecord):
        """
        Write colored line to console
        :param lr:
        :return:
        """
        msg = Formatter.format_record(lr)
        color = ConsoleWriter.log_level_2color(lr.level)
        cprint(msg, color)

