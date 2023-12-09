import aiofiles
from core.Template import Template
from core.Formatter import Formatter
from writers.AbstractWriter import AbstractWriter
from core.LogRecord import LogRecord


class FileWriter(AbstractWriter):
    """
    File writer
    """

    def __init__(self, name):
        super().__init__(name)
        self.io_file = None
        # TODO: Config.File.default_target()

    async def ensure_io_file(self, lr: LogRecord):
        if self.io_file is None:
            file_name = Template.format(template="/home/pavel/Log/test.log", provider=lr)
            self.io_file = await aiofiles.open(file=file_name, mode="w", encoding="utf8")

        return self.io_file

    async def write_record(self, lr: LogRecord):
        """
        Write log record to file(s)
        :param lr: log record
        :return:
        """
        line = Formatter.format_record(lr) + '\n'
        io_file = await self.ensure_io_file(lr)
        await io_file.write(line)
