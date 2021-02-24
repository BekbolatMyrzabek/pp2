#https://informatics.msk.ru/mod/statements/view.php?id=4163&chapterid=3835#1
'''
a = input().split()
j = 1000


for i in range(len(a)):   
    a[i] = int(a[i]) 
    if j > a[i]: 
        j = a[i]
    if a[i] > 0 and a[i] <= j:
        m = a[i]
        
print(m)
'''
i=list(input().split())
min=1000
for k in range(len(i)):
    s=int(i[k])
    if (s<min)and(s>0):
        min=s
print(min)
