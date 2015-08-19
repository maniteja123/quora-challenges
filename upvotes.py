n, k = map(int, raw_input().split())  
a = map(int, raw_input().split())

rightMostInc = range(n)  
rightMostDec = range(n)  
leftMostInc = range(n)  
leftMostDec = range(n)

for i in range(n):  
    if i>0:
        if a[i] >= a[i-1]: leftMostInc[i] = leftMostInc[i-1]
        if a[i] <= a[i-1]: leftMostDec[i] = leftMostDec[i-1]
    j = n-i-1
    if (j<n-1):     
        if a[j] <= a[j+1]: rightMostInc[j] = rightMostInc[j+1]
        if a[j] >= a[j+1]: rightMostDec[j] = rightMostDec[j+1]

sum = 0
print rightMostInc 
print rightMostDec 
print leftMostInc 
print leftMostDec
for i in range(n):  
    lInc = max([leftMostInc[i], i-k+1])
    lDec = max([leftMostDec[i], i-k+1])
    sum += (i-lInc+1)
    sum -= (i-lDec+1)
    if i-k >= 0:
        j = i-k
        rInc = min(rightMostInc[j], i-1)
        rDec = min(rightMostDec[j], i-1)
        sum -= (rInc-j+1)
        sum += (rDec-j+1)
    if i-k+1 >=0:
        print sum
