#!/usr/bin/env python3

from lampi.lampi_app import LampiApp
import pigpio

if __name__ == "__main__":
    pi = pigpio.pi()
    LampiApp(pi).run()
