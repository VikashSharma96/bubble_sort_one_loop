a = [123,1,2,1,1,6,7,8,9,6,0]
v = 0
for i in range(len(a)**2):
    if v == len(a)-1:
        v = 0 
    if a[v] > a[v + 1]:
        a[v],a[v+1] = a[v+1],a[v]
    v += 1
    print(a)
