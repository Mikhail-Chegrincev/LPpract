n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
mx = m[0]
for i in range(n):
    if m[i] > mx:
        mx = m[i]
print(mx)
print(m[::-1])