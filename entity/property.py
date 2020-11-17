class Property:
    def __init__(
        self,
        name: str,
        type_wanted: str,
        default_value: str = "",
    ):
        self.name = name
        self.type_wanted = type_wanted
        self.default_value = default_value
