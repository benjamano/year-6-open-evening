kitronik_servo_lite.set_distance_per_second(0.5)
basic.show_icon(IconNames.HAPPY)
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)

def on_forever():
    kitronik_servo_lite.drive_forwards(100)
basic.forever(on_forever)
