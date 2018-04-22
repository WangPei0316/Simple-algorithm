def fab(n):
    m,a,b = 0,1,1
    while m < n:
        yield a
        a,b = b,a+b
        m += 1


print(list(fab(10)))
