from core.LogRecord import LogRecord
from core.Config import Config
from writers.ConsoleWriter import ConsoleWriter
from writers.FileWriter import FileWriter
from writers.NullWriter import NullWriter

class Writer:
    def __init__(self):
        self.writers = dict()
        self.router = {}

        for rule in Config.rules():
            if not rule in self.router:
                self.router[rule] = list()

            for writer_name in Config.rule_writers(rule):
                writer = self.get_or_create_writer(writer_name)
                self.router[rule].append(writer)

    def get_or_create_writer(self, writer_name):
        if not writer_name in self.writers:
            self.writers[writer_name] = self.create_writer(writer_name)

        return self.writers[writer_name]

    async def write_record(self, lr : LogRecord):
        """
        Write log record to all writers
        """
        for writer in self.router[lr.writer]:
            print(f'[{writer.name}] <== {lr.message}')
            await writer.write_record(lr)

    @staticmethod
    def create_writer(writer):
        """
        Factory method - create writers by config
        """
        if writer == "console":
            return ConsoleWriter(writer)
        
        if writer == "file":
            return FileWriter(writer)

        if writer == "null":
            return NullWriter(writer)
