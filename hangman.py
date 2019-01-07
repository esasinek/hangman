from random import choice

words = ["andulka", "smrk", "televize", "jablko", "kominík", "řepa", "konvalinka", "sasanka", "křišťál"]
field = []
unsuccessful_tries = 0

def choose(list_of_words):
    chosen_word = choice(words)
    return chosen_word

word = choose(words)
for letter in word:
    field.append("_")

def show_current(field):
    print()
    print(" ".join(field))
    print()


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


def turn(field, tries):
    show_current(field)
    ch = (input("Napiš písmeno: ")).lower()        # character
    if ch in word:
        indices = [i for i, x in enumerate(word) if x == ch]    # tomuhle ještě úplně nerozumím
        for j in indices:
            field[j] = ch
    else:
        print("Špatně. Toto písmeno ve slovu není.")
        tries += 1
    return field, tries


def didhewinyet(current_field):
    if "_" in current_field:
        return False
    else:
        return True
