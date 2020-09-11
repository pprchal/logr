import threading
from enum import Enum
from project.sinks.httpSink.HttpSink import HttpSink
from project.presenters.ConsolePresenter import ConsolePresenter
from project.presenters.GUIPresenter import GUIPresenter
from project.storages.MemoryStorage import MemoryStorage


def thread_function(pat):
    pat.sink.start()

class PAT:
    def __init__(self, app):
        self.storages = [ MemoryStorage() ] 
        self.presenters = [ ConsolePresenter(), GUIPresenter(app) ]
        self.sink = HttpSink(self.presenters, self.storages)


    @classmethod
    def start(cls, app):
        pat = PAT(app)
        sinkThread = threading.Thread(target=thread_function, args=(pat,))
        sinkThread.start()
        return pat

