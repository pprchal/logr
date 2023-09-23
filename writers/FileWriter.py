from core.Formatter import Formatter
from writers.AffiliatedFile import AffiliatedFile
from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord


class FileWriter(AbstractWriter):
    """
    Resolving file writer - proxy for file rules
    Manages many affiliated_files and dispatch write_record requests by LogRecord.writer
    """
    def __init__(self, name):
        super().__init__(name)
        self.affiliated_files = {}

    async def write_record(self, lr: LogRecord):
        """
        Write log record to file(s)
        :param lr: log record
        :return:
        """
        affiliated_file = self.get_affiliated_file(lr)
        line = Formatter.format_record(lr) + '\n'
        await affiliated_file.write_line(line)

    def get_affiliated_file(self, lr: LogRecord):
        """
        Find affiliated file - by LogRecord.writer
        :param lr:
        :return:
        """
        if lr.writer in self.affiliated_files:
            return self.affiliated_files[lr.writer]

        affiliated_file = self.affiliated_files[lr.writer] = AffiliatedFile(lr)
        return affiliated_file


