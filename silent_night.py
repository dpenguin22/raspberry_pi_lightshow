
from lightshow_classes import Song

def silent_night():

    silent = Song(100)

    silent.name = "Silent Night"

    silent.notes.append([silent.g, silent.quarter*1.5])
    silent.notes.append([silent.a, silent.eigth])
    silent.notes.append([silent.g, silent.quarter])
    silent.notes.append([silent.e, silent.half*1.5])
    silent.notes.append([silent.g, silent.quarter*1.5])
    silent.notes.append([silent.a, silent.eigth])
    silent.notes.append([silent.g, silent.quarter])

    silent.notes.append([silent.e, silent.half*1.5])
    silent.notes.append([silent.d, silent.half])
    silent.notes.append([silent.d, silent.quarter])
    silent.notes.append([silent.b, silent.half*1.5])

    silent.notes.append([silent.c, silent.half])
    silent.notes.append([silent.c, silent.quarter])
    silent.notes.append([silent.g, silent.half*1.5])
    silent.notes.append([silent.a, silent.half])
    silent.notes.append([silent.a, silent.quarter])

    silent.notes.append([silent.c, silent.quarter*1.5])
    silent.notes.append([silent.b, silent.eigth])
    silent.notes.append([silent.a, silent.quarter])
    silent.notes.append([silent.g, silent.quarter*1.5])
    silent.notes.append([silent.a, silent.eigth])
    silent.notes.append([silent.g, silent.quarter])
    silent.notes.append([silent.e, silent.half*1.5])

    silent.notes.append([silent.a, silent.half])
    silent.notes.append([silent.a, silent.quarter])
    silent.notes.append([silent.c, silent.quarter*1.5])
    silent.notes.append([silent.b, silent.eigth])
    silent.notes.append([silent.a, silent.quarter])
    silent.notes.append([silent.g, silent.quarter*1.5])
    silent.notes.append([silent.a, silent.eigth])
    silent.notes.append([silent.g, silent.quarter])

    silent.notes.append([silent.e, silent.half*1.5])
    silent.notes.append([silent.d, silent.half])
    silent.notes.append([silent.d, silent.quarter])
    silent.notes.append([silent.f, silent.quarter*1.5])
    silent.notes.append([silent.d, silent.eigth])
    silent.notes.append([silent.b, silent.quarter])

    silent.notes.append([silent.c, silent.half*1.5])
    silent.notes.append([silent.e, silent.half*1.5])
    silent.notes.append([silent.c, silent.quarter])
    silent.notes.append([silent.g, silent.quarter])
    silent.notes.append([silent.e, silent.quarter])

    silent.notes.append([silent.g, silent.quarter*1.5])
    silent.notes.append([silent.f, silent.eigth])
    silent.notes.append([silent.d, silent.quarter])
    silent.notes.append([silent.c, silent.half*1.5])
    silent.notes.append([silent.c, silent.half*1.5])

    silent.size = len(silent.notes)
 
    return silent


