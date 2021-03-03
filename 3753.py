n = []
r = []

a, b = input().split()
a = int(a)
b = int(b)

for i in range(0,a):
    n.append(int(input()))
for j in range(0,b):
    r.append(int(input()))

print(len(list(set(n) & set(r))))   
print(*sorted(set(n) & set(r), key=int))
print(a - len(list(set(n) & set(r))))
print(*sorted(set(n) - set(r), key=int))
print(b - len(list(set(n) & set(r))))
print(*sorted(set(r) - set(n), key=int))