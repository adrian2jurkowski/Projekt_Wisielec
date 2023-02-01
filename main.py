import random

print('Witaj w programie "Wisielec". Podaj swój nick: ')
nick = input()

passwords = ['zeszyt', 'halogen', 'laptop', 'gwiazdka', 'interpretacja', 'github', 'kursor', 'wizualizacja', 'dogrywka',
             'kwas']

password = str(passwords[random.randint(0, len(passwords) - 1)])
tablica = list(password)

for i in range(len(password)):
    tablica[i] = '_'

attemp = 8

while attemp > 0:
    print()
    print(nick, "pozostało Ci ", attemp, "prób.")
    print()
    print(" ".join(tablica))
    print()

    print("Podaj swoją literę: ")
    letter = input()

    if letter in password:
        for i in range(len(password)):
            if password[i] == letter:
                tablica[i] = letter
        if "".join(map(str, tablica)) == password:
            print()
            print(nick, "pozostało Ci ", attemp, "prób.")
            print()
            print(" ".join(tablica))
            print()
            print(nick, "gratulacje! Wygrałeś.")
            break
    else:
        attemp -= 1
