class Vinyl:
    def __init__(self, album, artist, year):
        self.__album = album
        self.__artist = artist
        self.__year = year

    def display(self):
        print (self.__album + ' - ' + self.__artist + ' - ' + str(self.__year))

def run():
    ink_warantorn = Vinyl('INK', 'Waruntorn Paonil', 2022)
    ink_warantorn.display()
