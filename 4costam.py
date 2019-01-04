input = int(input("Podaj liczbe: "))
dzielniki = []

# [dzielniki.append(i) for i in range(1, input + 1) if input%i == 0]
print [i for i in range(1, input + 1) if input%i == 0]


