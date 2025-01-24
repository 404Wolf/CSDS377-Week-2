from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from typing import Any

from lampi import LampiDriver
from lampi.shared import State


class LampiLayout(BoxLayout):
    def update_saturation(self, saturation):
        State.driver.saturation = saturation
        self.update_color_box()

    def update_hue(self, hue):
        State.driver.hue = hue
        self.update_color_box()

    def update_brightness(self, brightness):
        State.driver.brightness = brightness
        self.update_color_box()

    def update_color_box(self):
        if self.ids.color_box:
            self.ids.color_box.color = State.driver.get_rgb()
            print(State.driver.get_rgb())


class LampiApp(App):
    def __init__(self, pi):
        super(LampiApp, self).__init__()

        State.driver = LampiDriver(pi)
        State.driver = LampiDriver(pi)
        State.driver.on = False
