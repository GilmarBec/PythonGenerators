import PySimpleGUI as Sg
from view.abstract_view import AbstractView


class PropertyView(AbstractView):
    CANCEL_BUTTON_TEXT = "Stop"

    def __init__(self):
        super().__init__()

    def create(self) -> dict:
        self.addRowToLayout([Sg.Text('Please enter property data')])
        self.addRowToLayout([Sg.Text('Name: ', size=(15, 1)), Sg.InputText(key='name')])
        self.addRowToLayout([Sg.Text('Type: ', size=(15, 1)), Sg.InputText(key='type_wanted')])
        self.addRowToLayout([Sg.Text("Default Value: ", size=(15, 1)), Sg.InputText(key='default_value')])
        return self.window(header="Creation of property")
