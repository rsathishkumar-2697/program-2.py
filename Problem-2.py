n = int(input())
result = []
f = 1
k = 0
for i in range(n):
    f += k
    result.append(f)
    k = 2

print(*result)