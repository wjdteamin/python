# 주민번호를 입력받아 태어난 년도를 출력하시오
# 태어난 년도는 주민
jumin = '001012-3035112'

this_year = 2024
born_year = None

if jumin[7] in ('1','2') :
    born_year = int('19'+jumin[0:2])
elif jumin[7] in ('3','4',) :
    born_year = int('20'+jumin[0:2])
else :
    print("다시입력해주세요")

age = this_year-born_year+1
print(f"현재 나이 : {age}")