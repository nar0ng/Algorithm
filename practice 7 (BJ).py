#1
'''
print('N: ', end='')
N =int(input())
print('X: ', end='')
X = int(input())
print('수열을 입력하세요: ',end='')
sequence = list(map(int,input().split()))

for i in range(N):
 if sequence[i]<X:
  print(sequence[i])
'''
#2
print('A: ', end='')
A=int( input())
print('B: ', end='')
B=int( input())

print('{}+{}={}'.format(A,B,A+B))
while (A and B) != 0:
 print('A: ', end='')
 A=int(input())
 print('B: ', end='')
 B=int(input())
 if (A or B) == 0:
  break
 print('{}+{}={}'.format(A, B, A + B))


