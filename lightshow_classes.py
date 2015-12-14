import RPi.GPIO as GPIO
import time


class Show:

    def __init__(self, outpins):
        pass
        GPIO.setmode(GPIO.BCM)
        for pin in range(len(outpins)):
            pass
            GPIO.setup(outpins[pin], GPIO.OUT)
            GPIO.output(outpins[pin], True)

    def turn_off(self, pin):
        pass
        GPIO.output(pin, True)

    def turn_on(self, pin):
        pass
        GPIO.output(pin, False)

    def all_off(self, outpins):
        for j in range(len(outpins)):
            pass
            GPIO.output(outpins[j], True)

    def all_on(self, outpins):
        for j in range(len(outpins)):
            pass
            GPIO.output(outpins[j], False)

    def twinkle(self, outpins, duration, interval):
        for j in range(int(duration / interval)):
            self.all_off(outpins)
            time.sleep(interval)
            self.all_on(outpins)
            time.sleep(interval)

    def finale(self, outpins, duration, interval):
        # Twinkle the lights for 5 seconds
        self.twinkle(outpins, 5, 0.5)

        # Hold all lights on for 5 seconds
        self.all_on(outpins)
        time.sleep(5)

        # Turn everything off for 2 seconds
        self.all_off(outpins)
        time.sleep(2)


class Song(object):
    # Define the notes to be used
    #c = 0
    #d = 1
    #e = 2
    #f = 3
    #g = 4
    #a = 5
    #b = 6
    e = 0
    f = 1
    g = 2
    a = 3
    b = 4
    c = 5
    d = 6
    rest = 7

    sixteenth = 0.25
    eigth = 0.5
    quarter = 1
    half = 2
    whole = 4

    def __init__(self,tempo):
        self.notes = []
        self.tempo = tempo
        
        # Define the duration of a beat based on the tempo
        self.onebeat = 60.0 / self.tempo
       
        # Set the minimum beat (this is really due to limitations in the relays
        self.minbeat = 0.1

        self.size = 0



