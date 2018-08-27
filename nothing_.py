
a = [8,5,6,4,9,1]
for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            # tmp = a[j]
            # a[j]=a[j+1]
            # a[j+1] = tmp
        print(a)

print(a)