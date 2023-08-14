def fib(n):
    if n == 1:
        print(n)
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)