H = int(input("숫자 입력1 : "))
M = int(input("숫자 입력2 : ")) 
t =0 
time = 45
if 0<= H <=23 and 0<= M and M<=59 :
    if M >= 45 :
        t =M -45
        print(f"{H}:{t}")
    elif M <45 and H > 0 :
        H =H-1
        t = (60 + M) - 45
        print(f"{H}:{t}")
    else : 
        H = 23
        t = (60 + M) - 45
        print(f"{H}:{t}")

else : 
    print("안됨")