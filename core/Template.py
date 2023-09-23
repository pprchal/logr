class Template:
    @classmethod
    def format(cls, template: str, provider):
        # writer is affiliation now - need to be refactored
        writer = provider.get_variable("writer")
        return template.replace("{{affiliation}}", writer)
