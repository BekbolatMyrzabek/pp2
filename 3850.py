l = input().split()
n = l.count('0')

for elem in filter(lambda x: x != '0', l):
    print(elem, end=' ')
for i in range(n):
    print(0, end=' ')