input = raw_input("Podaj jakies slowo, zdanie: ")
input = input.lower().replace(' ', '')
palindrom = input[::-1].lower().replace(' ', '')

print palindrom
print input

if palindrom == input:
    print("Twoje slowo jest palindromem")
else:
    print("NI CHU")