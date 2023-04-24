# s = set()
# while len(s) < 5:
#   num = int(input('0~9 사이 정수를 입력하세요 >>> '))
#   s.add(num)
  
# print("모두 입력되었습니다.")
# print(f'입력된 값은 {s} 입니다.')

# count = 1
# while count <= 100:  
#   i = 0
#   while i<10:
#     print("%-5d" % count, end='')
#     count += 1
#     i+=1
        
#   print()
  
  
dan = 2
num = 1
while num <= 9:
  while dan <= 9:      
    print("%-8s" % "{}x{}={}".format(dan, num, dan*num), end='')
    dan += 1
  
  print()  
  num += 1
  dan = 2
    
    
  