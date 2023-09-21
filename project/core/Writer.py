from project.core.LogRecord import LogRecord
from project.core.Config import Config
from project.writers.ConsoleWriter import ConsoleWriter
from project.writers.FileWriter import FileWriter
from project.writers.NullWriter import NullWriter

class Writer:
    def __init__(self):
        self.writers = self.create_writers()
        self.router = {}
        for writerName in Config.getWriters():
            for xx in Config.getWriterValues(writerName):
                ww = list(filter(lambda writer: writer.name == xx, self.writers))
                if not writerName in self.router:
                    self.router[writerName] = list()
                self.router[writerName].extend(ww)

    def write_record(self, lr : LogRecord):
        """
        Write log record to all writers
        """
        for writer in self.router[lr.writer]:
            writer.write_record(lr)

    def create_writers(self):
        """
        Factory method - create writers by config
        """
        writers = []
        for writer in Config.getDistinctWriters():
            if writer == "console":
                writers.append(ConsoleWriter(writer))
            
            if writer == "file":
                writers.append(FileWriter(writer))

            if writer == "null":
                writers.append(NullWriter(writer))
        
        return writers
