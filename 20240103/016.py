# 길이를 입력받아 센티미터면 인치로, 인치면 센티미터로 변경
# 1인치 = 2.54센티미터

length = int(input("길이 ? : "))
type = input("cm? inch? : ")

if type == 'cm':
    length = length /2.54
    print(f"{length}inch")
elif type == 'inch' :
    length = length *2.54
    print(f"{length}Cm")
else :
    print("단위를 다시 입력해주세요")
