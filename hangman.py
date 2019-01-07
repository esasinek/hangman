# přidat:
# - když uživatel prohraje, ukaž mu slovo



from random import choice

words = ["andulka", "smrk", "televize", "jablko", "kominík", "řepa", "konvalinka", "sasanka", "křišťál", "řeřicha", "kvásek", "kobyla", "kampaň", "šalvěj", "sárí"]

def choose(list_of_words):
    chosen_word = choice(words)
    return chosen_word


def make_it_the_field(word):
    field = []
    for letter in word:
        field.append("_")
    return field


def show_current(field):
    print()
    print(" ".join(field))
    print()


def turn(field, tries):
    show_current(field)
    ch = (input("Napiš písmeno: ")).lower()        # character
    list_of_letters = ["a", "á", "b", "c", "č", "d", "ď", "e", "é", "ě", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "ň", "o", "ó", "p", "q", "r", "ř", "s", "š", "t", "ť", "u", "ú", "ů", "v", "w", "x", "y", "ý", "z", "ž"]
    if ch in list_of_letters:
        if ch in word:
            indices = [i for i, x in enumerate(word) if x == ch]    # tomuhle ještě úplně nerozumím
            for j in indices:
                field[j] = ch
        else:
            print("Špatně. Toto písmeno ve slovu není. Stavím šibenici.")
            tries += 1
    else:
        print("To nebylo písmeno. Zkusíš to znovu?")
    return field, tries

def pick_picture(number_of_fails):
    if number_of_fails == 0:
        pass
    elif number_of_fails == 1:
        print("""





~~~~~~~
        """)
    elif number_of_fails == 2:
        print("""
+
|
|
|
|
|
~~~~~~~
        """)
    elif number_of_fails == 3:
        print("""
+---.
|
|
|
|
|
~~~~~~~
        """)
    elif number_of_fails == 4:
        print("""
+---.
|   |
|
|
|
|
~~~~~~~
        """)
    elif number_of_fails == 5:
        print("""
+---.
|   |
|   O
|
|
|
~~~~~~~
        """)
    elif number_of_fails == 6:
        print("""
+---.
|   |
|   O
|   |
|
|
~~~~~~~
        """)
    elif number_of_fails == 7:
        print("""
+---.
|   |
|   O
| --|
|
|
~~~~~~~
        """)
    elif number_of_fails == 8:
        print("""
+---.
|   |
|   O
| --|--
|
|
~~~~~~~
        """)
    elif number_of_fails == 9:
        print("""
+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~
        """)
    elif number_of_fails == 10:
        print("""
+---.
|   |
|   O
| --|--
|  / \\
|
~~~~~~~
        """)

def didhewinyet(current_field):
    if "_" in current_field:
        return False
    else:
        return True

# def new_game():
#     w = choose(words)
#     f = make_it_the_field(w)


print("""\nZahrajeme si hru Šibenice.\n
Budeš hádat, které slovo si myslím.\n
Pro začátek pár pravidel.
- Nezapomeň na diakritiku. Písmena "ž" a "z" nejsou to samé!
- Můžeš psát malá i velká písmena, výsledek bude stejný.
- Písmeno "ch" zadávej zvlášť jako "c" a "h". \n\nVšechno jasné? Tak hrajeme!\n""")

hra = "ano"
while hra == "ano":
    word = choose(words)
    field = make_it_the_field(word)
    unsuccessful_tries = 0
    try:
        print("""\nPřemýšlím...\n\nUž vím. Můžeš hádat.\nMáš 10 pokusů.\n""")
        while unsuccessful_tries < 10:
            field, unsuccessful_tries = turn(field, unsuccessful_tries)
            pick_picture(unsuccessful_tries)
            if unsuccessful_tries >= 10:
                hra = input(("Bohužel jsi prohrál. Správné slovo bylo '{}'.Chceš hrát znovu? Napiš ano/ne.\n").format(word)).lower()
                if hra == "ano":
                    print("\nNOVÁ HRA\n")
                    break
                elif hra == "ne":
                    raise ValueError("End of game")
                else:
                    print("To rozhodně nebylo ano.")
                    raise ValueError("End of game")
            elif didhewinyet(field) == True:
                    show_current(field)
                    hra = input("Gratulujeme! Vyhrál jsi. Chceš hrát znovu? Napiš ano/ne.\n").lower()
                    if hra == "ano":
                        print("\nNOVÁ HRA\n")
                        break
                    elif hra == "ne":
                        raise ValueError("End of game")
                    else:
                        print("To rozhodně není ano. Beru to tedy jako ne. Čau!")
                        raise ValueError("End of game")

    except ValueError as e:
        if e.args[0] == "End of game":
            print("Dobře, nebudu tě přemlouvat. Tak na viděnou příště!")
        else:
            raise
