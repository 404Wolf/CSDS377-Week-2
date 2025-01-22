from dataclasses import dataclass
import pigpio
from typing import Literal, Dict
from colorsys import hsv_to_rgb
from math import floor

LED_COLORS = ("red", "green", "blue")
LedColor = Literal["red", "green", "blue"]


class LampiDriver:
    """Driver for the Lampi"""

    @dataclass
    class LED:
        color: LedColor
        signal: int

    _leds: Dict[LedColor, LED]

    _on: bool = True
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

        for led in self._leds.values():
            pi.set_PWM_range(led.signal, 255)

    @property
    def saturation(self) -> int:
        """Returns the current saturation of the LED.

        Returns:
            int: The current saturation value, an int from 0 - 100.
        """
        return self._saturation

    @saturation.setter
    def saturation(self, value: int) -> None:
        """Sets the saturation of the LED, and updates the displayed color to match.

        Args:
            value (int): S from HSV. Value ranges from 0 - 100.
        """
        if value < 0 or value > 100:
            print("Invalid saturation value provided. Ignoring...")
            return None

        self._saturation = value
        self._update_lamp()
        return None

    @property
    def hue(self) -> int:
        """Returns the current hue value of the LED.

        Returns:
            int: The current hue
        """
        return self._hue

    @hue.setter
    def hue(self, value: int) -> None:
        """Sets the hue of the LED and causes the LED to update.

        Args:
            value (int): The H from HSV, a value from 0 to 360.
        """

        if value < 0 or value > 360:
            print("Invalid hue value provided. Ignoring...")
            return None

        self._hue = value
        self._update_lamp()
        return None

    @property
    def brightness(self) -> int:
        """Returns the current brightness of the LED

        Returns:
            int: The V from HSV of the LED's current value
        """
        return self._brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        """Sets the current brightness of the LED

        Args:
            value (int): The V from HSV, an integer from 0 - 100
        """

        if value < 0 or value > 100:
            print("Invalid brightness received. Ignoring...")
            return None

        self._brightness = value
        self._update_lamp()
        return None

    def get_rgb(self) -> tuple[int, int, int]:
        """Calculates the RGB representation of the current values of HSV.

        Returns:
            tuple[int, int, int]: The RGB of the current HSV values
        """
        scaled_h = self._hue / 360
        scaled_s = self._saturation / 100
        scaled_v = self._brightness / 100

        (r, g, b) = hsv_to_rgb(scaled_h, scaled_s, scaled_v)
        full_r = floor(r * 255)
        full_g = floor(g * 255)
        full_b = floor(b * 255)
        return (full_r, full_g, full_b)

    @property
    def on(self) -> int:
        """Returns whether the LED is currently on or not

        Returns:
            bool: True or False depending on whether the LED is on or not
        """
        return self._on

    @on.setter
    def on(self, value: bool) -> None:
        """Sets the LED to be on or off

        Args:
            value (bool): True to turn on, False to turn off
        """
        print("We are turning it on", value)
        self._on = value
        self._update_lamp()

    def _update_lamp(self) -> None:
        """Updates the lamp's LED to match the current internal state."""

        # If set to be off, turn off all LEDs and stop
        if not self._on:
            for led in self._leds.values():
                self._pi.set_PWM_dutycycle(led.signal, 0)

            return

        # Otherwise, determine the current RGB and set the LED accordingly
        (r, g, b) = self.get_rgb()
        self._pi.set_PWM_dutycycle(self._leds["red"].signal, r)
        self._pi.set_PWM_dutycycle(self._leds["green"].signal, g)
        self._pi.set_PWM_dutycycle(self._leds["blue"].signal, b)
