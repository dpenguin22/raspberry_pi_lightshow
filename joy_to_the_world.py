
from lightshow_classes import Song

def joy_to_the_world():

    joy = Song(160)

    joy.name = "Joy To The World"

    joy.notes.append([joy.c, joy.half])
    joy.notes.append([joy.b, joy.quarter+joy.eigth])
    joy.notes.append([joy.a, joy.eigth])
    joy.notes.append([joy.g, joy.half+joy.quarter])
    joy.notes.append([joy.f, joy.quarter])
    joy.notes.append([joy.e, joy.half])
    joy.notes.append([joy.d, joy.half])
    joy.notes.append([joy.c, joy.half+joy.quarter])
    joy.notes.append([joy.g, joy.quarter])         # Let

    joy.notes.append([joy.a, joy.half+joy.quarter])
    joy.notes.append([joy.a, joy.quarter])
    joy.notes.append([joy.b, joy.half+joy.quarter])
    joy.notes.append([joy.b, joy.quarter])
    joy.notes.append([joy.c, joy.half+joy.quarter])
    joy.notes.append([joy.c, joy.quarter])  # Let
    joy.notes.append([joy.c, joy.quarter]) 
    joy.notes.append([joy.b, joy.quarter]) 
    joy.notes.append([joy.a, joy.quarter]) 
    joy.notes.append([joy.g, joy.quarter]) 
    joy.notes.append([joy.g, joy.quarter+joy.eigth]) 
    joy.notes.append([joy.f, joy.eigth]) 
    joy.notes.append([joy.e, joy.quarter]) 
    joy.notes.append([joy.c, joy.quarter]) 

    joy.notes.append([joy.c, joy.quarter]) 
    joy.notes.append([joy.b, joy.quarter]) 
    joy.notes.append([joy.a, joy.quarter]) 
    joy.notes.append([joy.g, joy.quarter]) 
    joy.notes.append([joy.g, joy.quarter+joy.eigth]) 
    joy.notes.append([joy.f, joy.eigth]) 
    joy.notes.append([joy.e, joy.quarter]) 
    joy.notes.append([joy.e, joy.quarter])  # Let
    joy.notes.append([joy.e, joy.quarter])
    joy.notes.append([joy.e, joy.quarter])
    joy.notes.append([joy.e, joy.quarter])
    joy.notes.append([joy.e, joy.eigth])
    joy.notes.append([joy.f, joy.eigth])
    joy.notes.append([joy.g, joy.half+joy.quarter])
    joy.notes.append([joy.f, joy.eigth])    # Let
    joy.notes.append([joy.e, joy.eigth])
    joy.notes.append([joy.d, joy.quarter])
    joy.notes.append([joy.d, joy.quarter])
    joy.notes.append([joy.d, joy.quarter])
    joy.notes.append([joy.d, joy.eigth])
    joy.notes.append([joy.e, joy.eigth])

    joy.notes.append([joy.f, joy.half+joy.quarter])
    joy.notes.append([joy.e, joy.eigth])
    joy.notes.append([joy.d, joy.eigth])
    joy.notes.append([joy.e, joy.quarter])
    joy.notes.append([joy.c, joy.half])
    joy.notes.append([joy.a, joy.quarter])
    joy.notes.append([joy.g, joy.quarter+joy.eigth])
    joy.notes.append([joy.f, joy.eigth])
    joy.notes.append([joy.e, joy.quarter])
    joy.notes.append([joy.f, joy.quarter])
    joy.notes.append([joy.e, joy.half])
    joy.notes.append([joy.d, joy.half])
    joy.notes.append([joy.c, joy.whole])

    joy.size = len(joy.notes)
 
    return joy


