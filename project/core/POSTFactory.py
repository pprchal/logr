from project.core.Config import Config
from project.core.LogRecord import LogRecord

class POSTFactory:
    @classmethod
    def build_frombuild_from_post_url(cls, postData):
        writer = POSTFactory.find_writer_by_affiliation(postData)

        return LogRecord(
            postData['logger'],
            postData['level'],
            postData['message'],
            postData['time'],
            writer
        )

    @classmethod
    def find_writer_by_affiliation(cls, postData):
        affiliationKey = Config.getFileAffiliation()
        affiliationValue = None
        if affiliationKey in postData.keys():
            affiliationValue = postData[affiliationKey][0]

        if affiliationValue in Config.getWriters():
            return affiliationValue
        
        return "default"     

        
