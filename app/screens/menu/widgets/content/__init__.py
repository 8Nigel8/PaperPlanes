from app.screens.menu.widgets.content.online_mode import OnlineModeBox
from app.screens.menu.widgets.content.papers import PapersBox
from app.screens.menu.widgets.content.settings import SettingsBox
from app.screens.menu.widgets.content.statistic import StatisticBox

content = {
    'QUICK START': None,
    'PAPERS': PapersBox(),
    'ONLINE MODE': OnlineModeBox(),
    'SETTINGS': SettingsBox(),
    'STATISTIC': StatisticBox(),
    'EXIT': None
}
