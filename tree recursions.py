# fibonacci on tree recursions 0 1 1 2 3 5 8
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
terms=int(input("enter number of terms to print:"))
print(("fibonacci series........"))
for i in range(terms):
    print(fib(i),end=' ')