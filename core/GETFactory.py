from urllib import parse
from core.Config import Config
from core.LogRecord import LogRecord


class GETFactory:
    @classmethod
    def build_from_url(cls, url):
        parsed_url = parse.urlparse(url)
        GET_data = parse.parse_qs(parsed_url.query)
        writer = GETFactory.find_writer_by_affiliation(GET_data)
        return LogRecord(
            GET_data['logger'][0],
            GET_data['level'][0],
            GET_data['message'][0],
            GET_data['time'][0],
            writer
        )

    @classmethod
    def find_writer_by_affiliation(cls, GET_data):
        affiliationKey = Config.file_affiliation()
        affiliationValue = None
        if affiliationKey in GET_data.keys():
            affiliationValue = GET_data[affiliationKey][0]

        if affiliationValue in Config.rules():
            return affiliationValue
        
        return "default"     

        
