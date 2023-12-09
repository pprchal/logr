import os
import yaml
from core.Rule import Rule


class Config:
    """
    Configuration - like interface - static methods
    """
    config = None

    class Console:
        @staticmethod
        def colors():
            """
            Console color map
            :return:
            """
            return Config.config['console']['colors']

    class File:
        """
        File section
        """

        @staticmethod
        def file_template() -> str:
            """
            Template for log file
            :return: string
            """
            return Config.config['file']['file_template']

    class Http:
        """
        Http config section
        """

        @staticmethod
        def address() -> str:
            return Config.config['http']['address']

        @staticmethod
        def port() -> int:
            return int(Config.config['http']['port'])

    @staticmethod
    def targets():
        return Config.config['targets']

    @staticmethod
    def target_writers(target):
        return Config.config['targets'][target]

    @staticmethod
    def load():
        """
        Loads config, repair missing values - config is safe.
        Can throw exception, if there is unrecoverable error
        :return:
        """
        # load yml file
        full_path = os.getcwd() + os.sep + "config.yaml"
        with open(full_path, encoding="utf8") as f:
            Config.config = yaml.safe_load(f)

        # transform text rules to objects
        Config.rules = list(map(lambda rule: Rule(rule), Config.config["rules"]))
