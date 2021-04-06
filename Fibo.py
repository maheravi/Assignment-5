def seqfibo(n):
    if n <= 1:
        return n
    else:
        return seqfibo(n - 1) + seqfibo(n - 2)


fibo = list()


def show(terms):
    print("Fibonacci sequence:")
    for i in range(terms):
        a = seqfibo(i)
        fibo.append(a)
        Fibo = tuple(fibo)
    print(Fibo)


terms = int(input("Please enter number of sequance= "))
show(terms)
