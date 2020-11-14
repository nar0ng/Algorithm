#1
print('정수 x를 입력해주세요', end=' ')
x = int (input ())
print('정수 y를 입력해주세요', end=' ')
y = int (input ())

if (x > 0) and (y > 0):
    print ('제 1사분면 입니다.')
elif x>0 and y<0:
    print ('제 4사분면 입니다')
elif x<0 and y>0:
    print ('제 2사분면 입니다')
elif x<0 and y<0:
    print ('제 3사분면 입니다')
else:
    print ('잘못된 입력 입니다')

#2