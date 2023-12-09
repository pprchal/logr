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
        def file_template() -> str:
            """
            Template for log file
            :return: string
            """
            return Config.config['file']['file_template']

        @staticmethod
        def default_target() -> str:
            return Config.config['file']['default_target']

    class Rules:
        _affiliation_field_ = ""

        @staticmethod
        def affiliation_field() -> str:
            return Config.Rules._affiliation_field_

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

        field_rule = next((rule for rule in Config.config["rules"] if "field" in rule), None)
        if field_rule is not None:
            Config.Rules._affiliation_field_ = field_rule["field"]
