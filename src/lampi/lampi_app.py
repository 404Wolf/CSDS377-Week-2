from kivy.app import App
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty
from lampi import LampiDriver
from typing import cast


class LampiSlider(Slider):
    def __init__(self, **kwargs):
        super(LampiSlider, self).__init__(**kwargs)
        self.size_hint = (1, 0.33)


class LampiApp(App):
    def __init__(self, pi):
        super(LampiApp, self).__init__()
        self.driver = LampiDriver(pi)

    @property
    def saturation(self):
        return self.driver.saturation

    @saturation.setter
    def saturation(self, value: int):
        print("Setting saturation to", value)
        self.driver.saturation = value

    @property
    def hue(self):
        return self.driver.saturation

    @hue.setter
    def hue(self, value: int):
        print("Setting hue to", value)
        self.driver.saturation = value

    @property
    def brightness(self):
        return self.driver.brightness

    @brightness.setter
    def brightness(self, value: int):
        print("Setting brightness to", value)
        self.driver.brightness = value
