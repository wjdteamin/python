#국어, 영어 점수를 입력받아 합계와 평균을 출력
kor = int(input("국어 점수? : "))
eng = int(input("영어 점수? : "))
hap = kor + eng
avg = hap/2
print(f'합계 : {hap}점, 평균 : {avg}점')