import aiofiles
import os
from core.LogRecord import LogRecord
from core.Config import Config


class AffiliatedFile:
    def __init__(self, lr: LogRecord) -> None:
        self.writer = lr.writer
        if lr.writer == '':
            self.writer = Config.file_not_resolved()

        self.io_file = None
        self.fullPath = Config.file_dir() + os.sep + lr.writer + ".log"

    def is_affiliation_match(self, lr: LogRecord):
        return self.writer == lr.writer
    
    async def write_line(self, line):
        if self.io_file is None:
            self.io_file = aiofiles.open(file= self.fullPath, mode= "w", encoding="utf8") # open(file= fullPath, mode= "w", encoding="utf8")

        self.io_file.write(line)
        self.io_file.flush()
