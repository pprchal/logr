from urllib import parse
from core.LogRecord import LogRecord


class HttpParser:
    @classmethod
    def parse_from_json(cls, json):
        """
        Create LogRecord from json object
        :param json:
        :return:
        """
        return LogRecord(
            lambda prop_name: json[prop_name] if prop_name in json else "default"
        )

    @classmethod
    def parse_from_url(cls, url):
        """
        Create LogRecord from uri
        :param url:
        :return:
        """
        parsed_url = parse.urlparse(url)
        data = parse.parse_qs(parsed_url.query)

        return LogRecord(
            lambda prop_name: data[prop_name][0] if prop_name in data else "default"
        )
