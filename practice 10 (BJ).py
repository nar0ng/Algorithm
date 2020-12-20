cases = int(input())

for j in range(cases):
    a,b = map(int, input().split())
    AB = a+b
    print("Case #%s"%(j+1, AB))




x = int(input())
for i in range(x):
    num = list(map(int,input().split()))
    num.sort()
    print(num[-3])