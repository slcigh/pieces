# generator first n items of fibo
def fibo(lim):
    m, n = 1, 1
    while lim > 0:
        yield n
        m, n = n, m + n
        lim -= 1


print list(fibo(20))


