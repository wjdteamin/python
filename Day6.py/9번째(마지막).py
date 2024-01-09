# dictionary : 키와 값의 쌍
ice ={"바밤바" : 1000, "옥동자" : 1200, "월드콘" : 2000}
print(ice)

# Read 
print(ice["바밤바"])

# 월드콘 
print(ice["월드콘"])

# create 
ice['아맛나'] = 1100
ice['빵빠레'] = 1500
print(ice)

# 키와 값을 같이 주면 Create 라고 생각하면된다. 키만 주면 읽는다.

#update
ice['빵빠레'] = 1800
print(ice)

#delete
del ice['빵빠레']
print(ice)

# 키가 있으면 변경이고 키가 없으면 추가다. update와 create는 비슷하다.