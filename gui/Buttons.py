from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QAction, QGridLayout
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu,
                            SplitPushButton, SplitToolButton, PrimaryToolButton, PrimarySplitPushButton,
                            PrimarySplitToolButton, PrimaryDropDownPushButton, PrimaryDropDownToolButton,
                            TogglePushButton, ToggleToolButton, TransparentPushButton, TransparentToolButton,
                            TransparentToggleToolButton, TransparentTogglePushButton, TransparentDropDownToolButton,
                            TransparentDropDownPushButton, PillPushButton, PillToolButton, setCustomStyleSheet,
                            CustomStyleSheet)
from qfluentwidgets import FluentIcon as FIF


class ButtonView(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet("ButtonView{background: rgb(255,255,255)}")


class ToolButton(ButtonView):
    def __str__(self):
        super().__init__()

        self.menu = RoundMenu(parent=self)