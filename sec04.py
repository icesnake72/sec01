'''
sec04.py는 사용자 정의 함수 예제입니다.
'''
def add(a, b):
  """add 함수는 전달된 두 파라미터(정수만 가능)의 값을 더하여 리턴하는 함수입니다."""
  return a + b

def show(*args):
  for item in args:
    print( item )
    
def greet(msg='안녕하세요'):
  print(msg)
  

print(add("abc", "def"))
#print(add("abc", 1))

li = list()
li = [1,2,3]
print(li.__doc__)

# print(add(10, 10))

# show(123, '456', [7,8,9], (0,1,2), 'test')

# greet()
# greet('hello')