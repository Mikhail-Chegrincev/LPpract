n = int(input())
m = int(input())
A = []
for i in range(n):
    B = []
    for i in range(n):
        B.append(int(input()))
    A.append(B)
max = 0
row_max = 0
for i in range(len(A)):
    if max < A[i][i]:
        max = A[i][i]
        row_max = i
row_m = A[m]
A[m] = A[row_max]
A[row_max] = row_m
for i in A:
    print(' '.join(map(str, i)))