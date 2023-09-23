import aiofiles
import os
from core.LogRecord import LogRecord
from core.Config import Config


class AffiliatedFileWriter:
    """
    Leaf of routing graph. Physical file on disk
    """
    def __init__(self, lr: LogRecord):
        self.writer = lr.writer
        if lr.writer == '':
            self.writer = Config.file_not_resolved()

        self.io_file = None
        self.fullPath = Config.file_dir() + os.sep + lr.writer + ".log"

    def is_affiliation_match(self, lr: LogRecord):
        return self.writer == lr.writer

    async def write_line(self, line):
        """
        Write log line to affiliated file
        :param line:
        :return:
        """
        io_file = await self.ensure_io_file()
        await io_file.write(line)
        await io_file.flush()

    async def ensure_io_file(self):
        """
        Open writer file safe-way
        TODO: if file cannot be opened -> do nothing
        TODO: maybe write to memory and store as bulks. (no file locking)
        :return: aiofile
        """
        if self.io_file is None:
            self.io_file = await aiofiles.open(file=self.fullPath, mode="w", encoding="utf8")
        return self.io_file

