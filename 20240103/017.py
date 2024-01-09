# 임외로 가정
# 남자의 적정체중은 키 - 100  여자의 적정체중은 키 - 105 이다
# 키를 입력받아 적정체중을 출력하시오

hegith = int(input("길이 ? : "))
gender = input("남자 여자? : ")

if gender == '남자':
    hegith = hegith -100
    print(f"{hegith}Kg")
elif gender == '여자' :
    hegith = hegith -105
    print(f"{hegith}Kg")
else :
    print("셩별을 다시 입력해주세요")
