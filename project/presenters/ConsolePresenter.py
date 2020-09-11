from project.presenters.AbstractPresenter import AbstractPresenter
from project.core.LogRecord import LogRecord
from termcolor import colored, cprint
import os

class ConsolePresenter(AbstractPresenter):
    def __init__(self):
        os.system('color')
        print('ConsolePresenter')

    def presentLogRecord(self, lr: LogRecord):
        cprint(lr.asString(), self.logLevel2Color(lr.level))

