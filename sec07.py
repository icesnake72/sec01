'''
type checking and Code in python
Code Hint이며, 강제성(컴파일 오류를 일으키지 않음)이 없다.
'''
from typing import Final

number:int = 10
print(number)

strVal:str = "python"
print(strVal)

MC_YOO: Final = "유재석"
print(MC_YOO)

print()

# 
# 강제성이 없기 때문에 아래와 같이 해도 컴파일 에러가 발생하지 않는다.
MC_YOO = "강호동"
print(MC_YOO)

strVal = 1
print(strVal)

number = "안녕하세요 파이썬입니다."
print(number)