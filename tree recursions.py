# fibonacci on tree recursions 0 1 1 2 3 5 8
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
terms=int(input("enter number of terms to print:"))
print(("fibonacci series........"))
for i in range(terms):
    print(fib(i),end=' ')

OUTPUT:-
enter number of terms to print:20
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
