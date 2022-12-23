
from worker import task, MT

@task
def X(pm):
  w=pm[0]
  c=yield
  wait=c.mbox('BOX1', w)
  print("X waiting for BOX1 from Y")
  while wait():
      yield
  else:
      msg=c.get('BOX1')
      if not msg:
         print("X giving up on BOX1")
      else:
         print("X Get BOX1", msg)
         c.put('BOX2', (1,True,"X is OK"))
  return

@task
def Y(pm):
  w=pm[0]
  c=yield
  wait=c.mbox('BOX2', w)
  print("Y waiting for BOX2 from X")
  while wait():
      yield
  else:
      msg=c.get('BOX2')
      if not msg:
         print("Y giving up on BOX2")
      else:
         print("Y Get BOX2", msg)
         c.put('BOX1', (2,True,"Y is OK"))
  return

mt=MT()
#mt.worker(X,(500,))
#mt.worker(Y,(500,))
mt.worker(X,(0,))
mt.worker(Y,(0,))
mt.start()
print(mt.x)

