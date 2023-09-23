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
        def get_property(prop_name):
            if prop_name in json.keys():
                return json[prop_name]

            return "default"

        writer = cls.find_writer_by_affiliation(get_property)
        return LogRecord(
            property_provider=get_property,
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
        data = parse.parse_qs(parsed_url.query)

        def get_property(prop_name):
            if prop_name in data.keys():
                return data[prop_name][0]

            return "default"

        writer = cls.find_writer_by_affiliation(get_property)
        return LogRecord(
            property_provider=get_property,
            writer=writer
        )

    @classmethod
    def find_writer_by_affiliation(cls, prop_provider):
        affiliation_property_value = prop_provider(Config.File.affiliation())
        if affiliation_property_value in Config.rules():
            return affiliation_property_value

        return "default"





        
