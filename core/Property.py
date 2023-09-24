class Property:
    @staticmethod
    def int(name: str, default: int, props) -> int:
        value = Property.get(name=name, default="", props=props)
        try:
            return default if value == "" else int(value)
        except TypeError:
            print(f'Bad [int] property [{name}] = {value}')
            return default

    @staticmethod
    def get(name: str, default: str, props) -> str:
        return props[name] if name in props else default
