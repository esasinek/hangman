from hangman import *

print("""Zahrajeme si hru Šibenice.\n
Budeš hádat, které slovo si myslím. \nNezapomeň na diakritiku. Písmena "ž" a "z" nejsou to samé!
Můžeš psát malá i velká písmena.\n\nVšechno jasné? Tak hrajeme!\n\nPřemýšlím...\n\nUž vím. Můžeš hádat.
Máš 10 pokusů.\n""")

try:
    while unsuccessful_tries < 10:
        field, unsuccessful_tries = turn(field, unsuccessful_tries)
        pick_picture(unsuccessful_tries)
        if unsuccessful_tries >= 10:
            raise ValueError("Game Over")
        elif didhewinyet(field) == True:
            raise ValueError("Game Won")

except ValueError as e:
    if e.args[0] == "Game Over":
        print("Konec hry.")
    elif e.args[0] == "Game Won":
        print("Gratulujeme! Vyhrál jsi.")
    else:
        raise
