from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord


class NullWriter(AbstractWriter):
    def __init__(self, name):
        self.name = name

    async def write_record(self, lr:LogRecord):
        return
