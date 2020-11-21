from view.property_view import PropertyView
from entity.property import Property


class PropertyController:
    def __init__(self):
        self.view = PropertyView()

    def create(self) -> Property or None:
        request = self.view.create()

        if request is None:
            return None

        name = request.get("name")
        type_wanted = request.get("type_wanted")
        default_value = request.get("default_value")

        return Property(
            name=name,
            type_wanted=type_wanted,
            default_value=default_value,
        )
