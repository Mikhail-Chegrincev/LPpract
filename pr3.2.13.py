a, b = int(input()), int(input())
if a < b:
    x = 2 * a + 2 * b
elif a > b:
    x = a - b + 1
elif a == b:
    x = b**2 - 1
print(x)