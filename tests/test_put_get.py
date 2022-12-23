
from worker import task, MT

@task
def X(pm):
  i=0;c=yield
  wait=c.mbox('BOX1', 5*10)
  while wait():
      i+=1
      if i%25==0:print("X Waiting for mailbox BOX1 from Y", i)
      yield
  else:
      print("X Get BOX1", c.get('BOX1'))
      c.put('BOX2', (1,True,"OK"))
  return

@task
def Y(pm):
    c=yield;i=0
    wait=c.mbox('BOX2', 1*1000)
    while i<100:
       i+=1
       if i%25==0:print('Inside Y', i)
       yield
    else:
       c.put('BOX1', (2,"This is from Y"))
    while wait():
       print("Y Waiting for mailbox BOX2 from X");yield
    else:
       print("Y Get BOX2", c.get('BOX2'))
    return

mt=MT()
mt.worker(X,())
mt.worker(Y,())
mt.start()

