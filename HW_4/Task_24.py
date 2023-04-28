n = int(input())
col = list()
for i in range(n):
    x = int(input())
    col.append(x)

col_count = list()
for i in range(len(col) - 1):
    col_count.append(col[i-1] + col[i] + col[i+1])
col_count.append(col[-2] + col[-1] + col[0])
print(max(col_count))
