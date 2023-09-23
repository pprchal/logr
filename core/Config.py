import os
import yaml


class Config:
    config = None

    class Console:
        @classmethod
        def colors(cls):
            return Config.config['console']['colors']

    class File:
        """
        File section
        """
        @classmethod
        def flush(cls):
            """
            Flush after write?
            :return: string
            """
            return True

        @classmethod
        def name_template(cls):
            """
            Template for affi. file
            :return: string
            """
            return Config.config['file']['name_template']

        @classmethod
        def dir(cls):
            return Config.config['file']['dir']
    
        @classmethod
        def not_resolved(cls):
            return Config.config['file']['not_resolved']
    
        @classmethod
        def affiliation(cls):
            return Config.config['file']['affiliation']

    class Http:
        """
        Http config section
        """
        @classmethod
        def address(cls):
            return Config.config['http']['address']

        @classmethod
        def port(cls):
            return int(Config.config['http']['port'])
    
    @classmethod
    def rules(cls):
        return Config.config['rules']

    @classmethod
    def rule_writers(cls, rule):
        return Config.config['rules'][rule]

    @classmethod
    def enabled_writers(cls):
        """
        Get all writers as referenced by rules
        :return:
        """
        writers = set()
        for rule in Config.rules():
            for writer in Config.config['rules'][rule]:
                writers.add(writer)

        return list(writers)

    @classmethod
    def load(cls):
        full_path = os.getcwd() + os.sep + 'config.yaml'
        with open(full_path, encoding="utf8") as f:
            Config.config = yaml.safe_load(f)
