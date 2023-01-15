def toHexDigit(pin1: number, pin2: number, pin4: number, pin8: number):
    global digits, val
    digits = ["0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"]
    val = pin1 + 2 * pin2 + 4 * pin4 + 8 * pin8
    return digits[val]
val = 0
digits: List[str] = []
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_DOWN)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_DOWN)
basic.show_icon(IconNames.YES)

def on_forever():
    basic.show_string("" + (toHexDigit(pins.digital_read_pin(DigitalPin.P13),
        pins.digital_read_pin(DigitalPin.P14),
        pins.digital_read_pin(DigitalPin.P15),
        pins.digital_read_pin(DigitalPin.P16))), 50)
basic.forever(on_forever)
