import re


class Template:
    regex = r"{{([0-9a-zA-Z_]+)}}"

    @staticmethod
    def format(template: str, provider):
        replaced = re.sub(
            Template.regex,
            lambda match: Template.resolve_variable_value(match, provider),
            template
        )

        return replaced

    @staticmethod
    def resolve_variable_value(match, provider):
        name = match.group(1)
        variable_value = provider.get_variable(name)
        return variable_value
