n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
sr = 0 
for i in range(n):
    sr += m[i]
sr //= n
for i in range(n):
    if m[i] == 0:
        m[i] = sr
print(m)