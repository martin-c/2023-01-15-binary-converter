function toHexDigit (pin1: number, pin2: number, pin4: number, pin8: number) {
    digits = [
    "0",
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
    "F"
    ]
    val = pin1 + 2 * pin2 + 4 * pin4 + 8 * pin8
    return digits[val]
}
let val = 0
let digits: string[] = []
pins.setPull(DigitalPin.P13, PinPullMode.PullDown)
pins.setPull(DigitalPin.P14, PinPullMode.PullDown)
pins.setPull(DigitalPin.P15, PinPullMode.PullDown)
pins.setPull(DigitalPin.P16, PinPullMode.PullDown)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    basic.showString("" + (toHexDigit(pins.digitalReadPin(DigitalPin.P13), pins.digitalReadPin(DigitalPin.P14), pins.digitalReadPin(DigitalPin.P15), pins.digitalReadPin(DigitalPin.P16))))
    basic.pause(100)
})
