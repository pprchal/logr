from project.writers.AffiliatedFile import AffiliatedFile
from project.writers.AbstractWriter import AbstractWriter
from project.core.LogRecord import LogRecord

class FileWriter(AbstractWriter):
    def __init__(self, name):
        self.name = name
        self.affiliated_files = []

    def write_record(self, lr: LogRecord):
        affiliated_file = self.get_affiliated_file(lr)
        line = self.format_line(lr)
        affiliated_file.write_line(line)

    def get_affiliated_file(self, lr : LogRecord):
        for affiliated_file in self.affiliated_files:
            if affiliated_file.is_affiliation_match(lr):
                return affiliated_file
            
        affiliated_file = AffiliatedFile(lr)
        self.affiliated_files.append(affiliated_file)
        return affiliated_file

    def format_line(self, lr: LogRecord):
        return f"{lr.time}|{lr.level}|{lr.logger}|{lr.message}\n"
