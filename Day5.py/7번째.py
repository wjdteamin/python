list1 = [15,20,30,90,100,200,300]
# list1의 길이를 재라 -> len()

"""
a=0
for x in list1 : 
    a=a+1
print(a) 
"""
# 들여쓰기는 어딘가에 종속되어있어야한다. 

hap = 0
a = 0
for x in list1 :
    hap = x + hap
    a +=1
print(hap/a)