with open('vvod2.txt', 'r') as f:
    n = int(f.readline())
A = [[0]*n for i in range(n)]
a = 1
row = 0
column = -1
d_row = 0
d_column = 1
while a <= n**2:
    if  0 <= row + d_row < n and 0 <= column + d_column < n and A[row + d_row][column + d_column] == 0:
        row += d_row
        column += d_column
        A[row][column] = a
        a += 1
    else:
        if d_column == 1:
            d_column = 0
            d_row = 1
        elif d_row == 1:
            d_column = -1
            d_row = 0
        elif d_column == -1:
            d_column = 0
            d_row = -1
        else:
            d_column = 1
            d_row = 0
with open('vivod2.txt', 'w') as f:
    for i in A:
        f.write(' '.join(map(str, i)))
        f.write('\n')
