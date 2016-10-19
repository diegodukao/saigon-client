from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout

from random import choice
from uuid import uuid4

TEAMS = [
    "blue",
    "red",
]

ALIGNMENTS = [
    (1, 0, 0, 1),
    (0, 0, 1, 1),
    (1, 1, 1, 1),
]


class Board(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(25):
            button = WordButton(text="palavra", group="words")
            self.add_widget(button)


class WordButton(ToggleButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_disabled_down = ""
        self.background_disabled_normal = ""

    def on_press(self):
        self.disabled = True
        self.background_color = choice(ALIGNMENTS)


class SaigonClient(App):
    player_id = StringProperty()
    team = StringProperty()

    def on_start(self):
        self.player_id = str(uuid4())
        self.team = self.choose_team()
        self.root.board_screen.team_label.text = self.team

    def choose_team(self):
        return choice(TEAMS)


if __name__ == "__main__":
    SaigonClient().run()
