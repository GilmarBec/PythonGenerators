import PySimpleGUI as Sg
from view.abstract_view import AbstractView


class EntityView(AbstractView):
    def __init__(self):
        super().__init__()

    def create(self):
        self.layout = []

        self.addRowToLayout([
            Sg.Text('Class Name: ', size=(15, 1)),
            Sg.InputText(key='class_name')
        ])

        self.addRowToLayout([
            Sg.Text('Validator: ', size=(15, 1)),
            Sg.InputText(
                key='validator',
                tooltip="(default: self.validate_setter)"
            )
        ])

        return self.window(header="Creation of Class")

    def show_data(self, archive: list):
        self.layout = []

        for row in archive:
            self.addRowToLayout(row=[Sg.Text(row)])

        return self.window(header="Response Class")
