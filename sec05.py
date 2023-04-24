'''
sec05.py 파이썬에서 클래스와 객체
'''
import sec04

class player:
  def __init__(self):
    pass
    
  def __str__(self):
    return f'{self.name}({self.event})'
  
  def getName(self):
    return self.name
  
  def showName(self):
    print(self.name)
  
  def setName(self, name):
    self.name = name
    
  def setEvent(self, event):
    self.event = event
    

wizard = player()
wizard.setName('왕따우지')
wizard.setEvent('야구')
wizard.showName()
print(wizard)


print(sec04.add('a', 'b'))
