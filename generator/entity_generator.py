class EntityGenerator:
    def __init__(
        self,
        validator: str,
        properties: list or None = None,
        class_name: str = "",
    ):
        self.validator = validator
        self.properties = properties
        self.class_name = class_name

    def generate_entity(self) -> str:
        msg = self.header()
        msg += self.generate_init()
        msg += self.generate_setters_and_getters(tabs=1)
        return msg

    def generate_init(self) -> str:
        return self.init()

    def generate_setters_and_getters(self, tabs: int = 0) -> str:
        msg = ""
        for property in self.properties:
            msg += self.getter(
                name=property.name,
                type_wanted=property.type_wanted,
                tabs=tabs,
            )
            msg += self.setter(
                name=property.name,
                type_wanted=property.type_wanted,
                tabs=tabs,
            )

        return msg
    
    def header(self, extends_from: str = "") -> str:
        if extends_from != "":
            extends_from = f"({extends_from})"

        return f"class {self.class_name}{extends_from}:\n"

    def init(self) -> str:
        msg = "\tdef __init__(\n"
        
        for property in self.properties:
            default_value = ""
            type_wanted = ""

            if property.default_value != "":
                default_value = f" = {property.default_value}"

            if property.type_wanted != "":
                type_wanted = f": {property.type_wanted}"

            msg += f"\t\t{property.name}{type_wanted}{default_value},\n"
        
        msg += "\t):\n"

        for property in self.properties:
            msg += f"\t\tself.{property.name} = {property.name}\n"

        return msg + "\n"

    @staticmethod
    def getter(name: str, type_wanted: str, tabs: int = 1) -> str:
        out_logic_tab = "\t"*tabs
        in_logic_tab = "\t"*(tabs + 1)
        msg = f"{out_logic_tab}@property\n"
        msg += f"{out_logic_tab}def {name}(self) -> {type_wanted}:\n"
        msg += f"{in_logic_tab}return self.__{name}" + "\n\n"
        return msg

    def setter(self, name: str, type_wanted: str, tabs: int = 1) -> str:
        out_logic_tab = "\t"*tabs
        in_logic_tab = "\t"*(tabs + 1)
        msg = f"{out_logic_tab}@{name}.setter\n"
        msg += f"{out_logic_tab}def {name}(self, {name}) -> None:\n"
        msg += f"{in_logic_tab}" + self.validate(name, type_wanted) + "\n"
        msg += f"{in_logic_tab}self.__{name} = {name}" + "\n\n"
        return msg

    def validate(self, name: str, type_wanted: str) -> str:
        return f"{self.validator}({name}, {type_wanted})"
