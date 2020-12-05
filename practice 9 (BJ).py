'''
#평균 구하기
print('시험 본 과목의 개수: ', end='')
N =int(input())
score = list(map(int, input().split()))

M = 0

for i in range(N):
    if M < score[i]:
    M = score[i]

    for i in range(N):
    score[i] = (score[i]/M)*100

sum = 0
for i in range(N):
sum = sum + score[i]

print(sum / N)
'''

#숫자의 합
print('N개의 숫자:', end='')
N = int(input())
list_n = list(input())

sum = 0
for i in list_n:
    sum = sum+int(i)

print(sum)

