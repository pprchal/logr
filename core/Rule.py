import re
from core.Property import Property
from core.LogRecord import LogRecord


class Rule:
    def __init__(self, rule):
        if "field" in rule:
            self.is_re = False
            self.is_equal = rule["is_equal"]
            self.field = rule["field"]
        else:
            self.is_re = True
            self.re = re.compile(rule["re"])
        self.target = rule["target"]

    def is_match(self, lr: LogRecord):
        if self.is_re:
            return self.re.match(lr.line)

        field = Property.get(name=self.field, default="default", props=lr.properties)
        return self.is_equal == field
