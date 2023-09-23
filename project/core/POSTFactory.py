from project.core.Config import Config
from project.core.LogRecord import LogRecord

class POSTFactory:
    @classmethod
    def build_from_json(cls, jsonData):
        writer = POSTFactory.find_writer_by_affiliation(jsonData)
        return LogRecord(
            jsonData['logger'],
            jsonData['level'],
            jsonData['message'],
            jsonData['time'],
            writer
        )

    @classmethod
    def find_writer_by_affiliation(cls, jsonData):
        affiliationKey = Config.getFileAffiliation()
        affiliationValue = None
        if affiliationKey in jsonData.keys():
            affiliationValue = jsonData[affiliationKey][0]

        if affiliationValue in Config.getWriters():
            return affiliationValue
        
        return "default"     

        
