# collection(집합) 타입 : list, tuple, set, dictionary
# sequence(순서) 타입 : list, tuple

# list와 tuple의 차이점
# list는 mubatle(가변), tuple은 immutable(불변)

# list와 tuple은 sequence여서 하나씩 다 확인하려면 for문이 필요하다.
# 타입의 이름과 타입을 바구는 함수의 이름은 같다.
list1 = [1,3,5]
tuple1 = tuple(list1)
list1 = list(list1)
print(type(list1))

# 데이터가 있다 - > C(Create)- 추가  R(Read) - 읽기(하나씩)  U(Update) - 수정 D(Delete) -삭제
# U와 D는 찾아서 한다.
list1.append(100)
print(list1)
 
# for 변수 in 컬렉션 : 
for item in list1:
    print(item)

# pass는 넘어간다. 나중에 작성한다는 의미다.
# list1의 값들을 하나씩 꺼내서 item에 넣는다.

# for x  in  리스트
# x는 리스트에서 꺼내온 값들을 x에 하나씩 넣는다.


# 병렬 처리 -> 여러개를 동시에 처리한다. - 매우 어렵다.

#index(리스트에서 값의 위치로) Update 
list1[1] = 200
print(list1)

# delete -> 인덱스로 지운다. 사용자가 데이터가 어디에 있는지 알고 있어야한다. 
del list1[2] 
print(list1)

# remove -> 값을 가지고 지운다.
list1.remove(200)
print(list1)

# U,D를 하기 위해서는 R을 해야한다.
