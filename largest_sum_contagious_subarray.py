l = [1,2,3,-2,5]
size = len(l)
for i in range(size):
    for j in range(i):
        print(l[j]+l[i])
