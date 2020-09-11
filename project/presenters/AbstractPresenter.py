from abc import ABC,abstractmethod
from project.core.LogRecord import LogRecord
from project.core.Config import Config

class AbstractPresenter(ABC):
    @abstractmethod
    def presentLogRecord(self, lr: LogRecord):
        pass

    def logLevel2Color(self, level):
        if level in Config.getLevelDefs():
            return Config.getLevelDefs()[level]
            
        return "green"