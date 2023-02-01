import random

print('Witaj w programie "Wisielec". Podaj swój nick: ')
nick = input()

passwords = ['zeszyt', 'halogen', 'laptop', 'gwiazdka', 'interpretacja', 'github', 'kursor', 'wizualizacja', 'dogrywka',
             'kwas']

password = str(passwords[random.randint(0, len(passwords) - 1)])
board = list(password)

for i in range(len(password)):
    board[i] = '_'

attemp = 8

while attemp > 0:
    print()
    print(nick, "pozostało Ci ", attemp, "prób.")
    print()
    print(" ".join(board))
    print()

    print("Podaj swoją literę: ")
    letter = input()

    if letter in password:
        for i in range(len(password)):
            if password[i] == letter:
                board[i] = letter
        if "".join(map(str, board)) == password:
            print()
            print(nick, "pozostało Ci ", attemp, "prób.")
            print()
            print(" ".join(board))
            print()
            print(nick, "gratulacje! Wygrałeś.")
            break
    else:
        attemp -= 1
        if attemp == 0:
            print("Koniec gry. Niestety nie udało sie odgadnąć hasła.")
            print("Poszukiwanym hasłem było: ", password)

