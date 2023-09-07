from kivy.app import App
from kivy.lang import Builder

from app.screens.game.game_screen import GameScreen
from app.screens.menu.menu_screen import MenuScreen
from app.screens.menu.widgets.content import OnlineModeBox, PapersBox, SettingsBox, StatisticBox

from kivy.uix.screenmanager import ScreenManager


class MyScreenManager(ScreenManager):
    pass


class BrainTypeApp(App):
    def build(self):
        return Builder.load_file('PaperPlanes.kv')


if __name__ == '__main__':
    BrainTypeApp().run()
