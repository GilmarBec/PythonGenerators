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

    def __str__(self):
        return f"Property[{self.name}]: {self.type_wanted} = {self.default_value}\n"

    def init_format(self) -> str:
        type_wanted = ""
        default_value = ""

        if self.type_wanted != "":
            type_wanted = f": {self.type_wanted}"

        if self.default_value != "":
            default_value = f" = {self.default_value}"

        return f"{self.name}{type_wanted}{default_value}"

    def getter(self, tabs: int = 1) -> str:
        out_logic_tab = "\t" * tabs
        in_logic_tab = "\t" * (tabs + 1)

        msg = f"{out_logic_tab}@property\n"
        msg += f"{out_logic_tab}def {self.name}(self) -> {self.type_wanted}:\n"
        msg += f"{in_logic_tab}return self.__{self.name}" + "\n"

        return msg + "\n"

    def setter(self, validator: str, tabs: int = 1) -> str:
        out_logic_tab = "\t" * tabs
        in_logic_tab = "\t" * (tabs + 1)

        msg = f"{out_logic_tab}@{self.name}.setter\n"
        msg += f"{out_logic_tab}def {self.name}(self, {self.init_format()}) -> None:\n"
        msg += f"{in_logic_tab}" + self.validate(validator) + "\n"
        msg += f"{in_logic_tab}self.__{self.name} = {self.name}" + "\n"

        return msg + "\n"

    def validate(self, validator):
        return f"{validator}({self.name}, {self.type_wanted})"
