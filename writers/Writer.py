from core.Config import Config
from core.LogRecord import LogRecord
from writers.AbstractWriter import AbstractWriter
from writers.ConsoleWriter import ConsoleWriter
from writers.FileWriter import FileWriter
from writers.NullWriter import NullWriter


class Writer(AbstractWriter):
    """
    Dispatching writer. The class has its own set of writers
    """

    def __init__(self, name):
        """
        Constructor - prepare internal structures
        :param name: name of writer
        """
        super().__init__(name)
        writers = list()
        for rule in Config.rules:
            writer = self.create_writer(rule.target)
            writers.append(writer)
        self.writers = [w for w in writers]

    def print_config(self):
        """
        Prints config
        :return:
        """
        print("Active writers:")
        for writer in self.writers:
            print(f"{writer.name}")

    async def write_record(self, lr: LogRecord):
        """
        Write log record to all writers
        """
        for rule in filter(lambda r: r.is_match(lr), Config.rules):
            for writer in self.find_writers(rule.target):
                await writer.write_record(lr)

    def find_writers(self, writer_name):
        """
        Create writer - factory method
        :param writer_name: name of writer (console)
        :return: configured writer
        """
        return filter(lambda writer: writer.name == writer_name, self.writers)

    @staticmethod
    def create_writer(writer: str):
        """
        Factory method - create writers by config
        """
        match writer:
            case "console":
                return ConsoleWriter(writer)
            case None:
                return NullWriter(writer)

        return FileWriter(writer)
