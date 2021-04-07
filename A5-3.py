setA = set()
setB = set()

print("Caution! This program input is a set of number which splitted by the space between them : ")

n = input("Enter Set of array for A : ")
m = input("Enter Set of array for B : ")

a = n.split(' ')
for i in range(len(a)):
    setA.add(a[i])

b = m.split(' ')
for i in range(len(b)):
    setB.add(b[i])

print('The intersection of set A and B is:')
intersection = setA.intersection(setB)
print(intersection)

print('The union of set A and B is:')
union = setA.union(setB)
print(union)