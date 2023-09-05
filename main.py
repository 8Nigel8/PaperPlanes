from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager


class MyScreenManager(ScreenManager):
    pass


class BrainTypeApp(App):
    def build(self):
        return Builder.load_file('PaperPlanes.kv')


if __name__ == '__main__':
    BrainTypeApp().run()
