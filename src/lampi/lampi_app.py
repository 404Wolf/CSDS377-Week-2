from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.slider import Slider


class LampiSlider(Slider):
    def __init__(self, **kwargs):
        super(LampiSlider, self).__init__(**kwargs)
        self.size_hint = (1, 0.33)


class LampiApp(App):
    def __init__(self):
        super(LampiApp, self).__init__()

    # def build(self):
    # return Builder.load_file("./lampi/lampi.kv")
