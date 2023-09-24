from core.Config import Config
from core.Property import Property


class AffiliationResolver:
    @classmethod
    def find_writer_by_affiliation(cls, properties) -> str:
        """
        Resolve LOG entry
            [affiliation_field] = app   INFO|12.12.2012:12:30|Message|APP1 => APP1
            [affiliation_field] = level INFO|12.12.2012:12:30|Message|APP1 => INFO
        :param properties: 
        :return: 
        """
        affiliation = Property.get(name=Config.File.affiliation_field(), default="default", props=properties)
        if affiliation in Config.rules():
            return affiliation

        return "default"
