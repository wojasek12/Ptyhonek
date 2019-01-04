import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

[c.append(x) for x in a if x in b and x not in c]

print c
#
# list1 = random.sample(xrange(1, 101), 20)
# list1.sort()
# list2 = random.sample(xrange(1, 101), 25)
# list2.sort()
#
# list3 = []
#
# [list3.append(x) for x in list1 if x in list2]
# [list3.remove(obj) for obj in list3 if list3.count(obj) > 1]
#
# print list1
# print list2
#
# print list3