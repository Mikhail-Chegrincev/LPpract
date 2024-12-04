n = int(input())
def f(n, s = ''):
    s += str(n % 10)
    n //= 10
    if n != 0:
        return f(n, s)
    else:
        return int(s)
print(f(n))