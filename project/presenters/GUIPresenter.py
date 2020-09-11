from project.gui.Application import Application
from project.presenters.AbstractPresenter import AbstractPresenter
from project.core.LogRecord import LogRecord
from termcolor import colored, cprint
import tkinter as tk
import os

class GUIPresenter(AbstractPresenter):
    def __init__(self, app:Application):
        self.app = app
        print('GUIPresenter')

    def presentLogRecord(self, lr: LogRecord):
        self.app.tbLog.insert(tk.END, lr.message)
        cprint(lr.asString(), self.logLevel2Color(lr.level))


