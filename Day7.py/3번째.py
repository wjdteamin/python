#할일 관리 
todos = [
    {'tno': 1, 'title' : '할 일1', 'reg_day' : '2024-01-09', 'finish' : False},
    {'tno': 2, 'title' : '할 일2', 'reg_day' : '2024-01-09', 'finish' : False},
    {'tno': 3, 'title' : '할 일3', 'reg_day' : '2024-01-09', 'finish' : False}
]
tno = 2

#CRUD 

#Read  :전체 읽기, 1개 읽기
for todo in todos : 
    print(todo)

a = 0
# 찾았니 = False
#할일 번호를 입력받아 찾아서 출력 
input_tno = int(input("할일 번호 : "))
for todo in todos : 
    if todo['tno'] == input_tno : # 찾는다.
     a = 1
     # 찾았니 = True 
     print(todo)
     break
     # 이곳은 if문 안이다. 
       
    # 이곳은 if문이 끝나고 for문은 끝나지 않음.
print('안녕') # if문이 없으면 무조건 실행된다. 그래서 변수를 따로 생성해야한다. 
# 이곳이 for문이 끝난곳

# break가 끝나면 

if a == 0 : 
    print("할일을 찾을 수 없습니다.")

