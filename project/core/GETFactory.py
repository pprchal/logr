from urllib import parse
from project.core.Config import Config
from project.core.LogRecord import LogRecord

class GETFactory:
    @classmethod
    def build_from_url(cls, url):
        parsed_url = parse.urlparse(url)
        getData = parse.parse_qs(parsed_url.query)
        writer = GETFactory.find_writer_by_affiliation(getData)
        return LogRecord(
            getData['logger'][0],
            getData['level'][0],
            getData['message'][0],
            getData['time'][0],
            writer
        )

    @classmethod
    def find_writer_by_affiliation(cls, getData):
        affiliationKey = Config.getFileAffiliation()
        affiliationValue = None
        if affiliationKey in getData.keys():
            affiliationValue = getData[affiliationKey][0]

        if affiliationValue in Config.getWriters():
            return affiliationValue
        
        return "default"     

        
