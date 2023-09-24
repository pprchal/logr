import os
from itertools import product

import yaml


class Config:
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
            return Config.config['file']['affiliation_field']

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
    def enabled_writers():
        """
        Get all writers as referenced by rules
        :return:
        """
        writers = set()
        for rule in Config.rules():
            for writer in Config.config['rules'][rule]:
                writers.add(writer)

        return list(writers)

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
            yml = yaml.safe_load(f)
            # continue only with validated config
            Config.config = yml
