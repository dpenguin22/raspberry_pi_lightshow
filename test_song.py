
from lightshow_classes import Song

def test_song():

    test = Song(110)

    test.notes.append([test.c, test.whole*3])
    test.notes.append([test.d, test.whole*3])
    test.notes.append([test.e, test.whole*3])
    test.notes.append([test.f, test.whole*3])
    test.notes.append([test.g, test.whole*3])
    test.notes.append([test.a, test.whole*3])
    test.notes.append([test.b, test.whole*3])

    test.size = len(test.notes)
 
    return test


