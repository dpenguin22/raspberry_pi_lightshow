
from lightshow_classes import Song

def we_wish_you_a_merry_christmas():

    wish = Song(130)

    wish.name = "We Wish You A Merry Christmas"

    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.g, wish.eighth])
    wish.notes.append([wish.a, wish.eighth])
    wish.notes.append([wish.g, wish.eighth])
    wish.notes.append([wish.f, wish.eighth])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.a, wish.eighth])
    wish.notes.append([wish.b, wish.eighth])
    wish.notes.append([wish.a, wish.eighth])
    wish.notes.append([wish.g, wish.eighth])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])
    wish.notes.append([wish.d, wish.quarter])

    wish.notes.append([wish.b, wish.quarter])
    wish.notes.append([wish.b, wish.eighth])
    wish.notes.append([wish.c, wish.eighth])
    wish.notes.append([wish.b, wish.eighth])
    wish.notes.append([wish.a, wish.eighth])
    wish.notes.append([wish.g, wish.quarter])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.d, wish.eighth])
    wish.notes.append([wish.d, wish.eighth])
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
    wish.notes.append([wish.d, wish.eighth])
    wish.notes.append([wish.d, wish.eighth])
    wish.notes.append([wish.e, wish.quarter])
    wish.notes.append([wish.a, wish.quarter])
    wish.notes.append([wish.f, wish.quarter])
    wish.notes.append([wish.g, wish.half])

    wish.size = len(wish.notes)
 
    return wish


