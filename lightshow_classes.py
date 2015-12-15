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

    def play_song(self, outpins, mySong):
        prev_note = 0

        # Start with everything off        
        self.all_off(outpins)

        # Loop through each note
        for item in range(mySong.size):
            note = mySong.notes[item][0]

#            if DEBUG:
#                print 'New Note: ' + str(note) + ' ' + str(mySong.notes[item][1] * mySong.onebeat)

            if item > 0 and note == prev_note:
                # If this note is the same as the last, turn off
                # the note for a fraction of a beat
                self.turn_off(outpins[note])
                time.sleep(mySong.minbeat)
            prev_note = note

            # Turn on the current note
            self.turn_on(outpins[note])

            # Turn off the other notes
            for j in range(len(outpins)):
                if j != note:
                    self.turn_off(outpins[j])
            # Hold the note for the desired amount of time
            holdtime = mySong.notes[item][1] * mySong.onebeat
            if holdtime >= mySong.minbeat:
                time.sleep(holdtime)
            else: 
                time.sleep(mySong.minbeat)


class Song(object):
    # Define the notes to be used
    e = 0
    f = 1
    g = 2
    a = 3
    b = 4
    c = 5
    d = 6
    rest = 7  # This doesn't work yet

    # Define the notes in terms of beats, quarter note = 1 beat
    sixteenth = 0.25
    eigth = 0.5
    quarter = 1
    half = 2
    whole = 4

    def __init__(self,tempo):
        self.notes = []
        self.tempo = tempo
        self.name = " "
        
        # Define the duration of a beat based on the tempo
        self.onebeat = 60.0 / self.tempo
       
        # Set the minimum beat (this is really due to limitations in the relays
        self.minbeat = 0.1

        self.size = 0



