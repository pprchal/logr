from core.Config import Config


class AffiliationResolver:
    @classmethod
    def find_writer_by_affiliation(cls, properties):
        affiliation = properties[Config.File.affiliation()]
        if affiliation in Config.rules():
            return affiliation

        return "default"
