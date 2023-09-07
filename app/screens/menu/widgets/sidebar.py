from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from app.screens.global_elements.logo_label import LogoLabel


class Sidebar(BoxLayout):
    button_list = [
        'QUICK START',
        'PAPERS',
        'ONLINE MODE',
        'SETTINGS',
        'STATISTIC',
        'EXIT'
    ]

    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)
        logo = LogoLabel()
        self.add_widget(logo)
        self.button_generation(screen)

    def button_generation(self, screen):
        for button_name in self.button_list:
            btn = SidebarBtn(
                text=button_name,
                on_press=lambda x, content_box=button_name: screen.set_content(content_box)
            )
            self.add_widget(btn)


class SidebarBtn(Button):
    pass
