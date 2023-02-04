def getSum(value):
    res = 1
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res
for i in range(10, 10000):
    sum1 = getSum(i)
    sum2 = getSum(sum1)
    if sum2 == i and sum1 != sum2:
        print('Дружественные числа :' , i, sum1)
for a in range(10 , 10000):
    s=1
    k=2
    while k*k<=a:
        if a%k==0:
            s+=k
            m=a//k
            if m != k:
                s+=m
        k+=1
    if a==s:
        print('Совершенные числа :' , a)
