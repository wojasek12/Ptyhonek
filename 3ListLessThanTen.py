a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = ["maciek", "tomek"]

# for x in range(len(a)):
#     print a[x]
input = int(input("Podaj jakoms liczbe: "))
c = []

print(" ".join((map(str, a))))
print(" ".join(str(x) for x in a if x < input))
print[i for i in a if i < 5]


