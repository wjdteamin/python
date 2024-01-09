a = '345'
b = int(a)
c = float(a)
d = str(b)

ar = [3,4,5]
# ar을 tuple로 변환해  br에 저장
br = tuple(ar)

# 리시트에 원소를 추가한다 : append
# .은 멤버 연산자 
# append는 프리랜서가 아니라 ar에 소속된 함수 -> method
ar.append(10)
ar.insert(1,1000)
print(ar)

xr = (10,20,30)
# xr에 40을 추가한 다음 출력하시오
xr = list(xr)
xr.append(40)
xr = tuple(xr)
print(xr)