
from lightshow_classes import Song

def we_wish_you_a_merry_christmas():

    wish = Song(140)


    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.g, wish.eigth])
    wish.notes.append([wish.a, wish.eigth])
    wish.notes.append([wish.g, wish.eigth])
    wish.notes.append([wish.f, wish.eigth])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.a, wish.eigth])
    wish.notes.append([wish.b, wish.eigth])
    wish.notes.append([wish.a, wish.eigth])
    wish.notes.append([wish.g, wish.eigth])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])

    wish.notes.append([wish.b, wish.quarter])
    wish.notes.append([wish.b, wish.eigth])
    wish.notes.append([wish.c, wish.eigth])
    wish.notes.append([wish.b, wish.eigth])
    wish.notes.append([wish.a, wish.eigth])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.d, wish.eigth])
    wish.notes.append([wish.d, wish.eigth])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.g, wish.half])
    wish.notes.append([wish.d, wish.quarter])

    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.f, wish.half])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.d, wish.half])
    wish.notes.append([wish.a, wish.quarter])

    wish.notes.append([wish.b, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.d, wish.eigth])
    wish.notes.append([wish.d, wish.eigth])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.g, wish.half])

    wish.size = len(wish.notes)
 
    return wish

