from core.AffiliationResolver import AffiliationResolver


class LogRecord(object):
    def __init__(self, properties):
        self.properties = properties
        self.writer = AffiliationResolver.find_writer_by_affiliation(properties)

    def safe_get(self, name):
        return self.properties[name] if name in self.properties else ""

    @property
    def logger(self):
        return self.safe_get('logger')

    @property
    def level(self):
        return self.safe_get('level')

    @property
    def message(self):
        return self.safe_get('message')

    @property
    def time(self):
        return self.safe_get('time')

    def get_variable(self, name):
        if name == "writer":
            return self.writer

        return self.safe_get(name)
