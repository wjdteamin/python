numbers = [1,3,5,7]
# 그 숫자가 numbers에 있는지(True/False) 출력
num = 2
# print(num in numbers)

# 한번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찾았야한다. 
# 성공과 실패의 조건이 다르다. -> if ~ else ~ 가 아니다.
isFind = False
for item in numbers :
    if item == num : 
        print(True)
        isFind = True
if isFind== False: 
    print(False)

# 정석 필드(정석을 잘 사용하면 괜찮게 살 수 있다.)
# 디자인 패턴 : 설계 문제에 대한 해답을 문서화하기 위해 고안된 형식 방법
