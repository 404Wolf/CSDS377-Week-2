#!/usr/bin/env python3

if __name__ == "__main__":
    from lampi.lampi_app import LampiApp
    import pigpio

    pi = pigpio.pi()
    LampiApp(pi).run()
