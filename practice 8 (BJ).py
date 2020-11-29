
#윤년 구하기
'''
print('years: ', end='')
years=int(input())

if ((years%4 == 0) and (years%100 == 0)) or (years%400 == 0):
    print("1")
else:
    print("0")
'''

#셀프 넘버

def selfnumber():
   a=0
   for x in list(str(n)):
       a=a+int(x)

a=[]
for i in range(1,10001):
    k = selfnumber(i)
    a.append(k)

for b in range(1,10001):
    if b in a:
        pass
    else:
        print(b)


