from core.Formatter import Formatter
from writers.AffiliatedFileWriter import AffiliatedFileWriter
from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord


class FileWriter(AbstractWriter):
    """
    Resolving file writer - proxy for file rules
    Manages many files and dispatch write_record requests by LogRecord.writer
    """
    def __init__(self, name):
        super().__init__(name)
        self.affiliated_files = []

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
        for affiliated_file in self.affiliated_files:
            if affiliated_file.is_affiliation_match(lr):
                return affiliated_file
            
        affiliated_file = AffiliatedFileWriter(lr)
        self.affiliated_files.append(affiliated_file)
        return affiliated_file
