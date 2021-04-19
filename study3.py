# 점수 3개를 입력 받아서 평균 60 이상이면 '합격!' 을 출력하고, 그렇지 않은 경우엔 '불합격!' 을 출력하도록 프로그래밍 하시오
# 가장 작은 값이 40 미만이 아니면 합격 그렇지 않은 경우엔 불합격도 추가합니다.
# 정수 실수중 적절한 합수로 바꿔주는게 eval 함수입니다.

val_1 = eval(input("1과목 점수 입력: "))
val_2 = eval(input("2과목 점수 입력: "))
val_3 = eval(input("3과목 점수 입력: "))
avg = (val_1+ val_2 + val_3) /3
min_num = min(val_1, val_2, val_3)

if avg >=60 and min_num >= 40: # not(min_num <40)
    print("합격!")
else:
    print("불합격!")
