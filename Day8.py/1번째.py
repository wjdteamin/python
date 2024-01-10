# 나이를 입력받아 성년여부를 리턴하는 함수
"""
def age_status(nai : int):
    if nai>=18:
        print("성년입니다.")
    else : 
        print("미성년입니다.")

age_status(25)
"""

# 함수는 재사용하려고 사용하는 것이다. 상수와 비슷하다. 
# 함수는 작게 만드는 것이 좋다. 크게 만들면 사용하기가 힘들다. 

def is_adult(nai : int) :
    if nai >=18:
        return True
    else :
        return False

nai = 17
if is_adult(nai) == True:
    print("당신은 출입가능합니다.")
else : 
    print("집 가세요")

# 함수를 호출하려면 인수를 줘야한다. 결과를 항상 리턴을 줘야한다. 