with open('vvod1.txt', 'r') as f:
    m = int(f.readline())
    A = [list(map(int, line.split())) for line in f]
max = 0
row_max = 0
for i in range(len(A)):
    if max < A[i][i]:
        max = A[i][i]
        row_max = i
row_m = A[m]
A[m] = A[row_max]
A[row_max] = row_m
with open('vivod1.txt', 'w') as f:
    for i in A:
        f.write(' '.join(map(str, i)))
        f.write('\n')