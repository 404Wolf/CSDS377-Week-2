from dataclasses import dataclass
import pigpio
from typing import Literal, Dict

LED_COLORS = ("red", "green", "blue")
LedColor = Literal["red", "green", "blue"]


class LampiDriver:
    """Driver for the Lampi"""

    @dataclass
    class LED:
        color: LedColor
        signal: int

    _leds: Dict[LedColor, LED]

    _on: bool = False
    _saturation: int = 0
    _hue: int = 0
    _brightness: int = 0

    def __init__(self, pi: pigpio.pi, red_pin=19, green_pin=26, blue_pin=13):
        self._pi = pi
        self._leds = {
            "red": LampiDriver.LED("red", red_pin),
            "green": LampiDriver.LED("green", green_pin),
            "blue": LampiDriver.LED("blue", blue_pin),
        }

    @property
    def saturation(self) -> int:
        return self._saturation

    @saturation.setter
    def saturation(self, value: int) -> None:
        return None

    @property
    def hue(self) -> int:
        return self._hue

    @hue.setter
    def hue(self, value: int) -> None:
        return None

    @property
    def brightness(self) -> int:
        return self._brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        return None

    def get_rgb(self) -> tuple[int, int, int]:
        return (0, 0, 0)

    @property
    def on(self) -> int:
        return self._hue

    def turn_on(self):
        self._on = True

    def turn_off(self):
        self._on = False
