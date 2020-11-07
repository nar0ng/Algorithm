
#1-1
A=0
B=0
C=0
D=0

print('A의 값을 입력하시오: ', end ='')
A = int(input())
print('B의 값을 입력하시오: ', end = '')
B = int(input())

C=A+B
D=(A,B,C)

print(D, C)


#1-2
A=0
B=0
C=0
D=0

print('A의 값을 입력하시오: ', end ='')
A = int(input())
print('B의 값을 입력하시오: ', end = '')
B = int(input())

C=A+B
D=(B,A,C)

print(D, C)
