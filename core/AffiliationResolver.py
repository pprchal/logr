from core.Config import Config


class AffiliationResolver:
    @classmethod
    def find_writer_by_affiliation(cls, prop_provider):
        affiliation = prop_provider(Config.File.affiliation())
        if affiliation in Config.rules():
            return affiliation

        return "default"
