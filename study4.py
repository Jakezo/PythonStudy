# for 변수 in range(횟수):
#      반복할 코드

lst = [3, 6, 9]
for i in lst:
    print(i)

name = ['김일수', '김이수', '김삼수', '김사수','김오수']
score = [80, 67, 88, 50 ,44]
for i in range(5):
    if score[i] > 90:
        grade = "A"
    elif score[i]>= 80:
        grade = "B"
    elif score[i]>=70:
        grade = "C"
    elif score[i]>=60:
        grade = "D"
    else:
        grade = "F"
    print("{0}학생의 점수는 {1} 점이고, 등급은 {2} 입니다.".format(name[i],score[i],grade))


a = 2
b = 3
s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)   # 포멧함수 순서대로 넣는 방식이다.
print(s)

# 파이썬 한줄 삭제 Ctrl + Y 라인복사 Ctrl + D

# 정수를 입력 받아서 1부터 입력받은 정수까지 차례대로 1씩 증가하여 출력하도록 하는 프로그램이
num = int(input("정수입력:"))
for i in  range(1, num+1):     # range(1,10)  1부터 9까지의 숫자 범위를 나타낸다.
    print(i)
