import os
from itertools import product

import yaml


class Config:
    config = None

    class Console:
        @staticmethod
        def colors():
            return Config.config['console']['colors']

    class File:
        """
        File section
        """

        @staticmethod
        def flush():
            """
            Flush after write?
            :return: string
            """
            return True

        @staticmethod
        def name_template():
            """
            Template for affi. file
            :return: string
            """
            return Config.config['file']['name_template']

        @staticmethod
        def dir():
            return Config.config['file']['dir']

        @staticmethod
        def not_resolved():
            return Config.config['file']['not_resolved']

        @staticmethod
        def affiliation():
            return Config.config['file']['affiliation']

    class Http:
        """
        Http config section
        """

        @staticmethod
        def address():
            return Config.config['http']['address']

        @staticmethod
        def port():
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
        full_path = os.getcwd() + os.sep + 'config.yaml'
        with open(full_path, encoding="utf8") as f:
            Config.config = yaml.safe_load(f)
