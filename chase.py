import time
from lightshow_classes import Song

def chase(myShow,outpins):

    chase = Song(110)
    npins = len(outpins)

    # Turn on all lights one at a time
    for j in range(len(outpins)):
        myShow.turn_on(outpins[j])
        time.sleep(1)
    
    # Once they are all on, twinkle the lights and leave them on
    myShow.twinkle(outpins, 5.0, 0.5)
    myShow.all_on(outpins)
    time.sleep(2)

    for j in range(len(outpins)):
        myShow.turn_off(outpins[npins - j -1]) 
        time.sleep(0.2)
    time.sleep(3)

