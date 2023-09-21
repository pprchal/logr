import os
import yaml

class Config:
    config = None

    @classmethod
    def getLevelDefs(cls):
        return {
            'Debug': 'grey',
            'Error': 'red',
            'Info': 'green'
        }

    @classmethod
    def getFileDir(cls):
        return Config.config['file']['dir']
    
    @classmethod
    def getFileNotResolved(cls):
        return Config.config['file']['not_resolved']
    
    @classmethod
    def getFileAffiliation(cls):
        return Config.config['file']['affiliation']

    @classmethod
    def getHttpAddress(cls):
        return Config.config['http']['address']
    
    @classmethod
    def getHttpPort(cls):
        return int(Config.config['http']['port'])
    
    @classmethod
    def getWriters(cls):
        return Config.config['writers']

    @classmethod
    def getWriterValues(cls, writer):
        return Config.config['writers'][writer]

    @classmethod
    def getDistinctWriters(cls):
        writers = set()
        for writer in Config.getWriters():
            for writer in Config.config['writers'][writer]:
                writers.add(writer)

        return list(writers)

    @classmethod
    def load(cls):
        fullPath = os.getcwd() + os.sep + 'config.yaml'
        with open(fullPath, encoding="utf8") as f:
            Config.config = yaml.safe_load(f)
