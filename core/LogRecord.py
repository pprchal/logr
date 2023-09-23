from core.AffiliationResolver import AffiliationResolver


class LogRecord(object):
    def __init__(self, property_provider):
        self.property_provider = property_provider
        self.logger = property_provider('logger')
        self.level = property_provider('level')
        self.message = property_provider('message')
        self.time = property_provider('time')
        self.writer = AffiliationResolver.find_writer_by_affiliation(property_provider)

    def get_variable(self, name):
        # TODO: load all props into single dict.
        if name == "writer":
            return self.writer

        return self.property_provider(name)
