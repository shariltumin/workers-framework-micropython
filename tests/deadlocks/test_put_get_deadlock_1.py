
from worker import task, MT
from random import random

@task
def X(pm):
  w=pm[0]
  c=yield
  wait=c.mbox('BOX1', w)
  print("X waiting for BOX1 from Y")
  loop=True
  while loop:
     #print('x-w', w)
     if w==0:
        w=int((random()*10)+1)
     else:
        w=10000
     while wait() and w>0:
         yield
         w-=1
     else:
         msg=c.get('BOX1')
         if not msg:
            print("X giving up on BOX1")
            w=int((random()*10)+1)
            while w>0: yield; w-=1
            c.put('BOX2', (1,False,"X giving up"))
            yield
         else:
            print("X Get BOX1", msg)
            c.put('BOX2', (1,True,"X is OK"))
            loop=False
  return

@task
def Y(pm):
  w=pm[0]
  c=yield
  wait=c.mbox('BOX2', w)
  print("Y waiting for BOX2 from X")
  loop=True
  while loop:
     #print('y-w', w)
     if w==0:
        w=int((random()*10)+1)
     else:
        w=10000
     while wait() and w>0:
         yield
         w-=1
     else:
         msg=c.get('BOX2')
         if not msg:
            print("Y giving up on BOX2")
            w=int((random()*10)+1)
            while w>0: yield; w-=1
            c.put('BOX1', (1,False,"Y giving up"))
            yield
         else:
            print("Y Get BOX2", msg)
            c.put('BOX1', (2,True,"Y is OK"))
            loop=False
  return

mt=MT()
mt.worker(X,(500,))
mt.worker(Y,(500,))
#mt.worker(X,(0,))
#mt.worker(Y,(0,))
mt.start()
print(mt.x)

