# 년도를 입력받아 다음 윤년을 출력
# 2020입력 : 이번 윤년 그대로
# 2021입력 : 다음 윤년 2024년 

# try :
#     numbers = int(input('년도 입력 : '))
#     if numbers%4 != 0 : 
#         numbers = (numbers//4)* 4 + 4 

#     print(f'다음 윤년은 {numbers}년입니다')

# except : 
#     print("잘못된 입력 ")

# try :
#     numbers = int(input("달을 입력 : "))
#     if numbers == 2 : 
#      print(f"{numbers}월은 28일까지 있습니다.")
#     elif numbers in [4,6,9,11]:
#        print(f"{numbers}월은 30일까지 있습니다.")
#     elif numbers in [1,3,5,7,8,10,12]:
#        print(f"{numbers}월은 31일까지 있습니다.")
#     else :
#        print("없습니다.")
# except : 
#    print("잘못된 입력")


# 사각형의 너비와 높이를 입력받아 면적을 출력하는 함수 
# try :
#     width = float(input("너비 : "))
#     height = float(input("높이 : "))
#     area= width * height
#     print(round(area,1))
# except : 
#     print("너비와 높이를 제대로 입력하세요")

# 학생들의 이름과 나이가 적힌 명단이 있다. 이 명단을 파이썬 타입으로 표현하고 출력하시오.
# list=[ 
#     {"이름" : "우진", "나이" : 19},
#     {"이름" : "시은", "나이" : 20},
#     {"이름" : "제임스", "나이" : 19}
# ]
# print(list)

# 15번 문제
# number_list = [1, 2, 1, 1, 2, 3, 4, 1, 5, 2, 1, 5] 
# number_list = set(number_list)
# number_list = list(number_list)
# print(number_list)

# 아래와 같은 내용을 저장하는 파이썬 변수 s로 만드시오
    # 사는 곳 : 서울
    # 성별 : 여자
    # 이름 : 시은

    # 나이와 혈액형을 입력받아 저장 후 출력하시오
try:
    a = int(input("나이 : "))
    b = input("혈액형 : ")
    s = {"사는 곳" : "서울", "성별" : "여자" , "이름" : "시은" , "나이" : a, "혈액형" : b}
    print(s)
except : 
    print("잘못 입력하셨습니다.")