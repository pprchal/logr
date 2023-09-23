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
        return LogRecord(json)

    @classmethod
    def parse_from_url(cls, url):
        """
        Create LogRecord from uri
        :param url:
        :return:
        """
        parsed_url = parse.urlsplit(url)
        url_data = parse.parse_qsl(parsed_url.query)
        return LogRecord(dict(url_data))
