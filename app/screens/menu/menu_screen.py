from kivy.uix.screenmanager import Screen

from app.screens.menu.widgets.content import content
from app.screens.menu.widgets.content.content_box import ContentBox
from app.screens.menu.widgets.sidebar import Sidebar


class MenuScreen(Screen):
    sidebar = None
    content = None

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        self.content = ContentBox()
        self.add_widget(self.content)
        self.sidebar = Sidebar(self)
        self.add_widget(self.sidebar)

    def set_content(self, content_box_name):
        self.content.clear_widgets()
        self.content.add_widget(content[content_box_name])
