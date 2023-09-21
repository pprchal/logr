from project.writers.AbstractWriter import AbstractWriter
from project.core.LogRecord import LogRecord

class NullWriter(AbstractWriter):
    def __init__(self, name):
        self.name = name

    def write_record(self, lr:LogRecord):
        return