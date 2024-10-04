def f(n):
    d = []
    for i in range(2,n+1):
        k = 0
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                k += 1
                break
        if k == 0 and bin(i)[2:] == (bin(i)[2:])[::-1]:
            d.append(i)
    return d
print(f(int(input())))