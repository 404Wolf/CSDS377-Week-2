from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from lampi import LampiDriver


class LampiOnOffButton(Button):
    def __init__(self, **kwargs):
        super(LampiOnOffButton, self).__init__(**kwargs)
        self.size_hint = (1, 0.15)
        self.text = "On"

    def get_on_then_toggle(self):
        self.text = "On" if self.text == "Off" else "Off"
        return self.text == "On"


class LampiSlider(Slider):
    def __init__(self, **kwargs):
        super(LampiSlider, self).__init__(**kwargs)
        self.size_hint = (1, 0.33)


class LampiApp(App):
    def __init__(self, pi):
        super(LampiApp, self).__init__()
        self.driver = LampiDriver(pi)

        for attr in ["hue", "brightness", "saturation", "on"]:
            self._create_property(attr=attr)

    def _create_property(self, attr):
        def getter(self, attr=attr):
            return getattr(self.driver, attr)

        def setter(self, value, attr=attr):
            setattr(self.driver, attr, value)

        setattr(LampiApp, attr, property(getter, setter))
