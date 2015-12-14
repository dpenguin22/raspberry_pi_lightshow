import time
from joy_to_the_world import *
from jingle_bells import *
from deck_the_halls import *
from o_come_all_ye_faithful import *
from the_first_noel import *
from carol_of_the_bells import *
from hark_the_herald_angels_sing import *
from test_song import *
from chase import *
from lightshow_classes import Show, Song
import RPi.GPIO as GPIO

def play_song(myShow, mySong):

    prev_note = 0

    myShow.all_off(outpins)

    for item in range(mySong.size):
    
        note = mySong.notes[item][0]
        print 'New Note: ' + str(note) + '  ' + str(mySong.notes[item][1] * mySong.onebeat)

        if item > 0 and note == prev_note:
            # If this note is the same as the previous, turn
            # off all outputs for a fraction of a beat
            myShow.all_off(outpins)
            time.sleep(mySong.minbeat)
        prev_note = note

        # Turn on the current note
        myShow.turn_on(outpins[note])

        # Turn off the other notes
        for j in range(npins):
            if j != note:
                myShow.turn_off(outpins[j])

        # Hold the note for the desired amount of time
        holdtime = mySong.notes[item][1] * mySong.onebeat
	if holdtime >= mySong.minbeat: 
            time.sleep(holdtime)
        else:
            time.sleep(mySong.minbeat)


# Define the Pi output pins
npins = 7
outpins = [ [] for i in range(npins)]
outpins[0] = 17
outpins[1] = 25
outpins[2] = 23
outpins[3] = 8
outpins[4] = 24
outpins[5] = 27
outpins[6] = 22

# Create an instance of the Show class
myShow = Show(outpins)

# Load the songs
playlist = [ [] for i in range(5)]
playlist[0] = joy_to_the_world()
playlist[1] = jingle_bells()
playlist[2] = deck_the_halls()
playlist[3] = o_come_all_ye_faithful()
playlist[4] = the_first_noel()
playlist[5] = carol_of_the_bells()
playlist[6] = hark_the_herald_angels_sing()

# Start the loop to play the songs
while(True):
#    play_song(myShow, TEST_SONG)

    # Start with the chase program
    for i in range(2):
        chase(myShow, outpins)

    # Run the playlist 
    for i in range(len(playlist)):
        # Indicate which song in the playlist is being run
        for j in range(i):
            myShow_turn_on(outpins[j])
        myShow.all_off(outpins)
        # Play the song
        play_song(myShow, playlist[i])

        # Run the finale program
        myShow.finale(outpins, 5, 0.5)

    # Turn everything off
    myShow.all_off(outpins)
    time.sleep(20)

