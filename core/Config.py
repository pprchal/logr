import os
import yaml


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
        _affiliation_field_ = ""
        
        """
        File section
        """

        @staticmethod
        def flush() -> bool:
            """
            Flush after write?
            :return: bool
            """
            return True

        @staticmethod
        def path_template() -> str:
            """
            Template for log file
            :return: string
            """
            return Config.config['file']['path_template']

        @staticmethod
        def default_template() -> str:
            return Config.config['file']['default_template']

        @staticmethod
        def affiliation_field() -> str:
            return Config.File._affiliation_field_

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
    def rules():
        return Config.config['rules']

    @staticmethod
    def rule_writers(rule):
        return Config.config['rules'][rule]

    @staticmethod
    def load():
        """
        Loads config, repair missing values - config is safe.
        Can throw exception, if there is unrecoverable error
        :return:
        """
        # load yml file
        full_path = os.getcwd() + os.sep + 'config.yaml'
        with open(full_path, encoding="utf8") as f:
            Config.config = yaml.safe_load(f)

        Config.File._affiliation_field_ = Config.config['file']['affiliation_field']
