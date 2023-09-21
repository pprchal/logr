import os
from project.core.LogRecord import LogRecord
from project.core.Config import Config

class AffiliatedFile:
    def __init__(self, lr : LogRecord) -> None:
        self.writer = lr.writer
        if lr.writer == '':
            self.writer = Config.getFileNotResolved()

        fullPath = Config.getFileDir() + os.sep + lr.writer + ".log"
        self.io_file = open(file= fullPath, mode= "w", encoding="utf8")

    def is_affiliation_match(self, lr: LogRecord):
        return self.writer == lr.writer
    
    def write_line(self, line):
        self.io_file.write(line)
        self.io_file.flush()