import PySimpleGUI as Sg


class AbstractView:
    CANCEL = "Stop"
    SUBMIT = "Submit"

    CANCEL_BUTTON_TEXT = "Cancel"

    def __init__(self):
        self.layout = []

    def addRowToLayout(self, row):
        self.layout.append(row)

    def window(self, header, buttons=True):
        if buttons:
            self.addRowToLayout([
                Sg.Submit(),
                Sg.Cancel(button_text=self.CANCEL_BUTTON_TEXT)
            ])

        window = Sg.Window(title=header).Layout(rows=self.layout)
        button, values = window.Read()

        if button == self.CANCEL:
            return None

        return values
