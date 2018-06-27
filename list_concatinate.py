l1 = [1, 2, 3, 4, 5, 6, 11, 12, 13]

l2 = [6, 7, 8, 9, 0]

l3 = zip(l1, l2)

l3 = list(l3)
print(l3)
temp = max(len(l1), len(l2))
print(temp)
for r in range(len(l3), temp):
    print(r)
    l3.append(('', l1[r]))

print(l3)
