n = int(input("Enter number of rows: "))

a = [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(1,i):
        a[i][j] = (a[i - 1][j - 1] + a[i - 1][j])

print('The khayyam triangle for', n, ' number of rows is: ')

for i in range(n):
    print()
    for j in range(n - i + 1):
        print(end=" ")
    for j in range(0, i+1):
        print(a[i][j], end=" ")
