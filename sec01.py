'''
collection
list
tuple
set
dictionary
'''

li1 = []
li2 = list()
li3 = [1,2,3]
print(li3)      # [1,2,3]
li3.append(4)   # 추가 메소드
print(li3)      # [1,2,3,4]
li3.insert(3, 4)  # 4번째 인덱스에 4를 추가
print(li3)      # [1,2,3,4,4]
li3.remove(4)   # 리스트에서 첫번째 나오는 숫자 4를 제거
print(li3)      # [1,2,3,4]
li3.pop()       # 제일 뒤에 한 아이템을 제거
print(li3)
li3.pop(1)
print(li3)
li1 = li3.copy()
li1.append(2)
li1.append(5)
li1.append(4)
print(li1)
li1.sort()
print(li1)
li1.reverse()
print(li1)
li1.append(3)
print(li1.count(3))
print(type(li1))
print(type(li1[0]))

me = 10
print(id(me))

me += 1
print(id(me))