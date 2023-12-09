import aiofiles
from core.Template import Template
from core.LogRecord import LogRecord
from core.Config import Config


class AffiliatedFile:
    """
    Leaf of routing graph. Physical file on disk
    """

    def __init__(self, lr: LogRecord):
        self.writer = lr.writer
        if lr.writer == '':
            self.file_name = Template.format(template=Config.File.default_target(), provider=lr)

        self.file_name = self.create_file_name(lr)
        self.io_file = None

    async def write_line(self, line):
        """
        Write log line to affiliated file
        :param line:
        :return:
        """
        io_file = await self.ensure_io_file()
        await io_file.write(line)
        if Config.File.flush():
            await io_file.flush()

    async def ensure_io_file(self):
        """
        Open writer file safe-way
        TODO: if file cannot be opened -> do nothing
        TODO: maybe write to memory and store as bulks. (no file locking)
        :return: aiofile
        """
        if self.io_file is None:
            self.io_file = await aiofiles.open(file=self.file_name, mode="w", encoding="utf8")

        return self.io_file

    @staticmethod
    def create_file_name(lr: LogRecord):
        """
        Create file name for affiliated file from template
        :param lr:
        :return:
        """
        return Template.format(template=Config.File.file_template(), provider=lr)
