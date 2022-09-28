kitronik_servo_lite.setDistancePerSecond(0.5)
basic.showIcon(IconNames.Happy)
let strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
basic.forever(function () {
    kitronik_servo_lite.driveForwards(100)
})
