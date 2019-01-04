import random
while(True):

    input = int(raw_input("Podaj co wybierasz: \n1. Papier\n2.Nozyczki\n3.Kamien\n"))
    random1 = random.randint(1, 3)
    difference = input - random1
    if difference in [1, -2]:
        print("Wygrales!")
        continue
    elif difference in [-1, 2]:
        print("Przegrales")
        continue
    else:
        print("Remis ziomek")
        continue
