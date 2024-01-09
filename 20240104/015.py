# 주민번호를 입력받아 성별을 출력

jumin = '971012-1035112'
print(jumin[7])

if jumin[7] in ('1','3','5') :
    print("남성")
elif jumin[7] in ('2','4','6') :
    print("여성")
else :
    print("다시입력해주세요")