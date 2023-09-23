from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord


class NullWriter(AbstractWriter):
    """
    The best writer in the universe
    """
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    async def write_record(self, lr: LogRecord):
        """
        The most complex code
        :param lr:
        :return:
        """
        return
