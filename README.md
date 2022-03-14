# **Liquid Crystal Display (LCD) Library for RP2040 - Raspberry Pi Pico**
This package can be used in RP2040s to interface with a HD44780 LCD without I2C, UART, or SPI.

## Installation
Since this is a package for [MicroPython](https://micropython.org/) and it's supposed to be used with a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/), you can copy the `liquid_crystal_pico.py` file and load it into Thonny and your microcontroller.

## Quick Start
A simple example running on a [Wokwi Emulator](https://github.com/wokwi) can be found [here](https://wokwi.com/arduino/projects/314638477337559617).

```python
from liquid_crystal_pico import LiquidCrystalPico
from machine import Pin

rs = Pin(0, Pin.OUT)
e  = Pin(1, Pin.OUT)
d4 = Pin(2, Pin.OUT)
d5 = Pin(3, Pin.OUT)
d6 = Pin(4, Pin.OUT)
d7 = Pin(5, Pin.OUT)

lcd = LiquidCrystalPico(rs, e, d4, d5, d6, d7)
lcd.move_to(0,1)
lcd.write("Hello, Pico!")
```

## Features/Functions
```python
def clear()
def cursor_home()
def cursor_move_back()
def cursor_move_forward()
def display_blink_off()
def display_blink_on()
def display_off()
def display_on()
def display_shift_text_left()
def display_shift_text_right()
def move_cursor_left()
def move_cursor_right()
def move_to(line, column)
def write(string)
```

## In Progress/Roadmap
- [ ] Convert all binary numbers to constants
- [ ] Flexible support for configuration of LCD

## Bugs
Bugs or suggestions? Open an issue [here](https://github.com/gusandrioli/liquid-crystal-pico/issues/new).
