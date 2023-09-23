from core.AffiliationResolver import AffiliationResolver


class LogRecord(object):
    def __init__(self, property_provider):
        self.logger = property_provider('logger')
        self.level = property_provider('level')
        self.message = property_provider('message')
        self.time = property_provider('time')
        self.writer = AffiliationResolver.find_writer_by_affiliation(property_provider)
