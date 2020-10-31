# 세 자리수 X 세 자리 수

print('첫번째 세 자리 수를 입력해주세요>', end='')
fir = int(input ())


print('두 번째 세 자리 수를 입력해주세요>', end='')
sec = int(input ())

print(fir)
print(sec)

result1=fir*((sec%100)%10)
result2=fir*((sec%100)//10)
result3=fir*(sec//100)
result4=fir*sec

print(result1)
print(result2)
print(result3)
print(result4)

# 알람 시계
print('시간을 입력해주세요>', end='')
H = int(input ())

print('분 입력해주세요>', end='')
M = int(input ())

if M>= 45:
    print(H, M-45)
else:
    print(H-1, (60+M)-45)


