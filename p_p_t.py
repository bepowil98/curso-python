import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("computer_wins => ", computer_wins)
    print("user_wins => ", user_wins)

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()


    if not user_option in options:
        print("Esa opcion no es valida, elige otra opcion")
        continue
    rounds += 1

    computer_option = random.choice(options)
    print("user option => ", user_option)
    print("computer option => ", computer_option)

    if user_option == computer_option:
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a Tijera")
            print("User gano! ")
            user_wins += 1
        else:
            print("Papel gana a Piedra")
            print("computer gano! ")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra! ")
            print("User gano! ")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print("Computer gano! ")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("user gano! ")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("computer gano! ")
            computer_wins += 1
    if computer_wins == 2:
        print("Computer gano el juego")
        break

    if user_wins == 2:
        print("user gano el juego")
        break

