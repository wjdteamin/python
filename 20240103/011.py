# 반지름을 입력받아 원의 면적(파이* 반지름 * 반지름)을 출력
# 반지름을 입력받아 원둘레(2파이*반지름)을 출력

PI = 3.14

length = int(input("반지름 : ? "))

면적 = PI*length*length
원둘레 = 2*PI*length

print(f"면적 : {면적} 원둘레 : {원둘레}")