from entity.class_entity import Entity
from controller.property_controller import PropertyController
from view.entity_view import EntityView
import os
import datetime


class EntityController:
    def __init__(self):
        self.view = EntityView()

    def create(self):
        request = self.view.create()

        class_name = request.get("class_name")

        if class_name is None:
            print("fail")
            return None

        validator = request.get("validator")

        if validator is None or validator == "":
            validator = "self.validate_setter"

        entity = Entity(
            class_name=class_name,
            validator=validator,
            properties=self.get_properties()
        )

        self.view.show_data(archive=entity.entity_as_array())

        self.create_archive(entity)

    @staticmethod
    def get_properties():
        properties = {}

        while True:
            prop = PropertyController().create()

            if prop is None:
                return properties

            properties[prop.name] = prop

    @staticmethod
    def create_archive(entity: Entity):

        date = datetime.datetime.now().strftime("%Y_%m_%d")
        archive = f"result_classes/{date}"
        os.makedirs(name=archive, exist_ok=True)
        f = open(f"{archive}/{entity.class_name.lower()}.py", "w")

        f.write(entity.entity_as_string())
        f.close()
