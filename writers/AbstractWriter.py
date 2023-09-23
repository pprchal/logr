from abc import ABC,abstractmethod
from core.LogRecord import LogRecord


class AbstractWriter(ABC):
    """
    Base class for all writers
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def write_record(self, lr: LogRecord):
        pass

    def is_writer_match(self, lr: LogRecord):
        return self.name == lr.writer