'''
sec06.py 파이썬에서 쓰레드
'''

import threading
import random


def worker(name, li):
  """쓰레드에서 실행할 작업"""
  for item in li:
    print(f'{name}번째 쓰레드 : {item}')
  
  print()
    
threads = []
for item in range(5):
  t = threading.Thread(target=worker, args=(item, [random.randint(1,10) for i in range(5)]))
  threads.append(t)
  t.start()
  

for t in threads:
  t.join()
  
  
