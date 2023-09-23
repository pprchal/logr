from urllib import parse
from core.Config import Config
from core.LogRecord import LogRecord


class HttpFactory:
    @classmethod
    def build_from_json(cls, json):
        """
        Create LogRecord from json object
        :param json:
        :return:
        """
        def prop_provider(prop_name):
            return cls.get_property_value(prop_name, json)

        writer = cls.find_writer_by_affiliation(prop_provider)
        return LogRecord(
            property_provider=prop_provider,
            writer=writer
        )

    @classmethod
    def build_from_url(cls, url):
        """
        Create LogRecord from uri
        :param url:
        :return:
        """
        parsed_url = parse.urlparse(url)
        get = parse.parse_qs(parsed_url.query)

        def prop_provider(prop_name):
            return cls.get_property_value_list(prop_name, get)

        writer = cls.find_writer_by_affiliation(prop_provider)
        return LogRecord(
            property_provider=prop_provider,
            writer=writer
        )

    @classmethod
    def get_property_value_list(cls, prop_name, data):
        """
        Get property from bag - safe way
        :param prop_name:
        :param data:
        :return:
        """
        if prop_name in data.keys():
            return data[prop_name][0]

        return "default"

    @classmethod
    def get_property_value(cls, prop_name, json):
        """
        Get property from bag - safe way
        :param prop_name:
        :param json:
        :return:
        """
        if prop_name in json.keys():
            return json[prop_name]

        return "default"

    @classmethod
    def find_writer_by_affiliation(cls, prop_provider):
        affiliation_property_value = prop_provider(Config.file_affiliation())
        if affiliation_property_value in Config.rules():
            return affiliation_property_value

        return "default"





        
