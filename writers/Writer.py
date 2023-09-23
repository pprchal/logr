from core.LogRecord import LogRecord
from core.Config import Config
from writers.AbstractWriter import AbstractWriter
from writers.ConsoleWriter import ConsoleWriter
from writers.FileWriter import FileWriter
from writers.NullWriter import NullWriter


class Writer(AbstractWriter):
    """
    Dispatching writer. The class has its own set of writers
    """
    def __init__(self, name):
        super().__init__(name)
        self.writers = dict()
        self.router = self.build_router()

    def print_config(self):
        """
        Prints config
        :return:
        """
        print("Active writers:")
        for writer_name in self.writers:
            print(f'{writer_name} = {self.writers[writer_name]}')

    def build_router(self):
        """
        Create router table
        :return: router table APP1 => [console, file]
        """
        router = {}
        for rule in Config.rules():
            if not rule in router:
                router[rule] = list()

            for writer_name in Config.rule_writers(rule):
                writer = self.get_or_create_writer(writer_name)
                router[rule].append(writer)
        return router

    def get_or_create_writer(self, writer_name):
        """
        Create writer - factory method
        :param writer_name: name of writer (console)
        :return: configured writer
        """
        if not writer_name in self.writers:
            self.writers[writer_name] = self.create_writer(writer_name)

        return self.writers[writer_name]

    async def write_record(self, lr: LogRecord):
        """
        Write log record to all writers
        """
        for writer in self.router[lr.writer]:
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


