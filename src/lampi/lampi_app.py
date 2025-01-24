from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from lampi import LampiDriver
from lampi.shared import State


class LampiLayout(BoxLayout):
    def update_saturation(self, saturation):
        self.ids.color_box.color = State.driver.get_rgb()
        State.driver.saturation = saturation

    def update_hue(self, hue):
        self.ids.color_box.color = State.driver.get_rgb()
        State.driver.hue = hue

    def update_brightness(self, brightness):
        self.ids.color_box.color = State.driver.get_rgb()
        State.driver.brightness = brightness


class LampiApp(App):
    def __init__(self, pi):
        super(LampiApp, self).__init__()

        State.driver = LampiDriver(pi)
        State.driver = LampiDriver(pi)
        State.driver.on = False
