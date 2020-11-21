from generator.entity_generator import EntityGenerator
from entity.property import Property

print("==================================================")

class_name = input("Class Name: ")
validator = input("Validator(default: self.validate_setter): ")

if validator == "":
    validator = "self.validate_setter"

print("--------------------------------------------------")

properties = []
while True:
    for prop in properties:
        print(prop)

    name = input("Property name: ")
    type_wanted = input("Property type: ")
    default_value = input("Default Value(if don't have just press enter): ")

    properties.append(
        Property(
            name=name,
            type_wanted=type_wanted,
            default_value=default_value,
        )
    )

    if input("Add another Property(y/N)?") in ("", "n", "N"):
        break

    print("          ------------------------------          ")

print("==================================================")

generator = EntityGenerator(
    properties=properties,
    validator=validator,
    class_name=class_name.capitalize()
)

f = open(f"result_classes/{class_name.lower()}.py", "w")

f.write(generator.generate_entity())
f.close()
