from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Board(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(25):
            button = Button(text="palavra")
            self.add_widget(button)


class SaigonClient(App):
    pass


if __name__ == "__main__":
    SaigonClient().run()
