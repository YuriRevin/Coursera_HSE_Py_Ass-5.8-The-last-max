l = list(map(int, input().split()))
a, b = l[0], 0
for i in range(1, len(l)):
    if l[i] >= a:
        a, b = l[i], i
print(a, b)
