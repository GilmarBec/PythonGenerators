class Entity:
    def __init__(self, class_name: str, validator: str, properties: dict):
        self.class_name = class_name.capitalize()
        self.validator = validator
        self.properties = properties

    def __str__(self):
        return f"Class {self.class_name}"

    def entity_as_string(self) -> str:
        msg = f"class {self.class_name}:\n"
        msg += self.generate_init()
        msg += self.generate_getter_and_setter()

        return msg

    def generate_init(self) -> str:
        msg = "\tdef __init__(\n"

        for prop in self.properties.values():
            msg += f"\t\t{prop.init_format()},\n"

        msg += "\t):\n"

        for prop in self.properties.values():
            msg += f"\t\tself.{prop.name} = {prop.name}\n"

        return msg + "\n"

    def generate_getter_and_setter(self) -> str:
        msg = ""
        for prop in self.properties.values():
            msg += prop.getter()
            msg += prop.setter(self.validator)

        return msg

    def entity_header(self):
        return f"class {self.class_name}:"

    def entity_as_array(self) -> list:
        return self.entity_as_string().split("\n")
