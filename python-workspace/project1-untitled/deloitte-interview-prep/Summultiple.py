def multipleSum(n,x,y):
    nList = list(range(n+1))
    sumlist =[]
    for i in nList:
        if i%x == 0 or i%y==0:
            sumlist.append(i)
    total =0
    for j in range(0, len(sumlist)):
        total = total + sumlist[j]
    return total

print(multipleSum(15,1,12))