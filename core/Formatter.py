from core.LogRecord import LogRecord


class Formatter:
    @staticmethod
    def format_record(lr: LogRecord):
        """
        Format line for write
        TODO: let's configure in config.yml
        :param lr:
        :return:
        """
        return f"{lr.time}|{lr.level}|{lr.logger}|{lr.message}"
