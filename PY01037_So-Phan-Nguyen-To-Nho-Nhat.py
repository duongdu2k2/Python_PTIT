a = list(range(20000001))
a[:] = [0]*20000001
for i in range(1,20000001):
    for j in range(i,20000001,i):
        a[j] += 1
max = 0
check = []
for i in range(20000001):
    if a[i] > max:
        max = a[i]
        check.append(i)

# for i in check:
#     print(i,end=',')
t = int(input())
while t:
    n = int(input())
    for i in check:
        if i >= n:
            print(i)
            break
    t -= 1

    # 1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040,7560,10080,15120,20160,25200,27720,45360,50400,55440,83160,110880,166320,221760,277200,332640,498960,554400,665280,720720,1081080,1441440,2162160,2882880,3603600,4324320,6486480,7207200,8648640,10810800,14414400,17297280