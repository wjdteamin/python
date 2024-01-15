# 문자열을 자라서 사용하면 될거 같은디?

string = "동서남북동서남북동서남북"
# print(string[0]*4)
# #print(string[::4]) 동이 3개여서 4개가 나올 수 없다.
# print(string[0::2])
# print(string[0:4])

# 5번 문제
# print(string[::-1])
# print(string[::-2])
# print(string[-2::-2])

# 6번문제 replace
# phone = '010-1234-56578'
# a =phone.replace('-','.')
# print(a)

# 7번 문제
# 예외처리 try~ expcept ~
# try :
#     numbers = int(input("정수 입력 : "))
#     numbers = abs(numbers)
#     if numbers % 2 == 0:
#         print("짝수입니다.")
#     else :
#         print("홀수입니다.")
# except :
#     print("정수 입력해주세요.")


# 8번 문제 

# numbers = int(input('년도 입력  : '))
# try : 
#     if numbers % 4 == 0 :
#         print('올림픽 열립니다.')
#     elif numbers % 4 == 2 :
#         print('월드컵 열립니다.')
#     else :
#         print('둘 다 열리지 않습니다.')
# except :
#     print('제대로 입력해주세요')


# try :  - 문제를 잘못 이해했다.
#     world_cup_year = int(input('월드컵 : '))
#     olympic_year = int(input('올림픽 : '))
#     WORLD_CUP = 1930
#     OLYMPIC  = 1896
#     while True :
         
#          if world_cup_year == WORLD_CUP or  olympic_year ==OLYMPIC :
#              if world_cup_year == WORLD_CUP and olympic_year !=OLYMPIC :
#                 print("올해 월드컵이 열립니다.")
#                 break
#              elif world_cup_year != WORLD_CUP and olympic_year ==OLYMPIC :
#                 print("올해 올림픽이 열립니다.")
#                 break
#              else :
#                  print("둘 다 열립니다.")
#                  break
             
#          elif world_cup_year < WORLD_CUP and olympic_year < OLYMPIC :
#              print("둘 다 열리지 않습니다.")
#              break
#          WORLD_CUP = int(WORLD_CUP) +4
#          OLYMPIC = int(OLYMPIC) +4
# except : 
#     print("잘못된 입력입니다.")

# try : 
#     world_cup_year = int(input('월드컵 : '))
#     olympic_year = int(input('올림픽 : '))
#     WORLD_CUP = 2026
#     OLYMPIC  = 2024
#     while True :
#         if world_cup_year == WORLD_CUP :
#             print("올해 월드컵이 열립니다.")
#         elif olympic_year ==OLYMPIC :
#             print("올해 올림픽이 열립니다.")
#         elif 

# except : 
#     print("잘못된 입력입니다.")





# 9번 문제 - 윤년여부
# try : 
#     leap_year = int(input("년도 입력 : "))
#     if leap_year % 4 ==0 and leap_year % 100 != 0 : 
#         print("윤년이다.")
#     else :
#         print("윤년이 아니다.")
# except : 
#     print("잘못된 입력")

# try : 
#      leap_year = int(input("년도 입력 : "))
#      if leap_year % 4 ==0 and leap_year % 100 != 0 : 
#         print("윤년이다.")
#      else :
#          print("윤년이 아니다.")
# except : 
#      print("잘못된 입력")

# 10번 문제 
try:
     numbers = int(input('년도 입력 : '))
     if numbers % 4 == 0 : # 2의 배수도 포함된다. 그래서 안된다?
         print(f'{numbers+4}년이 다음 올림픽이 열리는 해입니다.')
     else :
        a = 4- (numbers%4) 
        print(f'{numbers+a}년이 다음 올림픽이 열리는 해입니다.')
except:
     print("잘못된 입력입니다.")

# 또 다른 방식 -> 몫을 가지고 구한다. 
# (numbers // 4) * 4  + 4 => 나머지를 싹 버리고 딱 나눠떨어지게 만들어서 거기에 다시 4를 
# 곱해서 4를 더해주면 된다.