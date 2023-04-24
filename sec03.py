'''
for 반복문은 보통 문자열 또는 collection(시퀀스, 비시퀀스) 또는 range()함수와 함께 사용된다.
'''

li = [1,2,3,4,5,6]
for num in li:
  print(num)
  
li = ['korea', 'usa', 'japan', 'china', 'france']
for country in li:
  print(country)
  
tp = ('python', 'c', 'java', 'c++', 'sql')
for lang in tp:
  print(lang)
  
s1 = {'baseball', 'soccer', 'basketball', 'ballyball', 'golf'}
for sport in s1:
  print(sport)
  
dic = {'유재석':'개그맨', '정우성':'배우', '이정재':'배우', 'BTS':'가수'}
for key in dic:
  print(key)
  print(key, dic[key], sep=':')
  
for num in range(5):
  print(num)
  
for num in range(1,11):
  print(num)
  
print()

for num in range(1, 11, 2):
  print(num)
  
print()

string = 'hello python'
for ch in string:
  print(ch)
  

for num in range(5,0,-1):
  print(num)
  
# hap = 0
# in_num = int(input('임의의 양수를 입력하세요 >>> '))
# for num in range(in_num+1):
#   hap += num
  
# print(f'1부터 {in_num}사이 모든 정수의 합계는 {hap}입니다')
# li = []
# num_of_fruit = int(input('몇 개의 과일을 보관할까요? >>> '))
# for item in range(1,num_of_fruit+1):
#   fruit = input(f'{item}번째 과일을 입력하세요 >>> ')
#   li.append(fruit)
  
# print(f'입력받은 과일들은 {li} 입니다')

score = []
exam = [99, 83, 100, 91, 86, 90, 59, 100, 76, 55]
for tmp in exam:  
  score.append( min(100, tmp+5) )

print(score)

ten = 0
dan = 0
string = ''
li = []
for num in range(0,100, 10):
  li = [num+i for i in range(1,11)]
  for item in li:
    ten = item // 10
    dan = item % 10
    if ten%3==0 and ten: 
      string = '짝'
    if dan%3==0 and dan:
      string += '짝'   
    
    print('%-10s' % f'{string if len(string) else item}', end='')
    string = ''
  
  print()
  
    
    