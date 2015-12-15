import time
from joy_to_the_world import *
from jingle_bells import *
from deck_the_halls import *
from o_come_all_ye_faithful import *
from the_first_noel import *
from carol_of_the_bells import *
from hark_the_herald_angels_sing import *
from silent_night import *
from we_wish_you_a_merry_christmas import *
from test_song import *
from chase import *
from lightshow_classes import Show, Song
import RPi.GPIO as GPIO

# Define global variables
DEBUG = 0

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
playlist = [ [] for i in range(9)]
playlist[0] = joy_to_the_world()
playlist[1] = jingle_bells()
playlist[2] = deck_the_halls()
playlist[3] = o_come_all_ye_faithful()
playlist[4] = the_first_noel()
playlist[5] = carol_of_the_bells()
playlist[6] = hark_the_herald_angels_sing()
playlist[7] = silent_night()
playlist[8] = we_wish_you_a_merry_christmas()

# Start the loop to play the songs
while(True):
#    play_song(myShow, TEST_SONG)

    # Start with the chase program
    for i in range(2):
        chase(myShow, outpins)

    # Run the playlist 
    for i in range(len(playlist)):
        # Indicate which song in the playlist is being run
        if i <= len(outpins):
            for j in range(i):
                myShow.turn_on(outpins[j])
        else:
            for j in range(i-npins):
                myShow.turn_on(outpins[npins-j-1])
            
        time.sleep(1)
        myShow.all_off(outpins)
        time.sleep(1)

        # Play the song
        #play_song(myShow, playlist[i])
        myShow.play_song(outpins, playlist[i])

        # Run the finale program
        myShow.finale(outpins, 5, 0.5)

    # Turn everything off
    myShow.all_off(outpins)
    time.sleep(10)

