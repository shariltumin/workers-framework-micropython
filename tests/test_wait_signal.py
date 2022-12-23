
# test_wait_signal.py
from worker import task, MT

@task
def X(pm):
  c=yield; i=0; keep=True
  event="T0-event-25"
  wait=c.mbox('x1', 5*1000)
  while wait():
      i+=1
      if i%500==0:print("X waiting for event on x1", i)
      yield
  else:
      trig=c.get('x1',keep)
      print('Event @X.x1:', trig)
      if event==trig:
         print('Event happened')
         c.put('y1', "S0-event-71")
  return

@task
def Y(pm):
    c=yield;i=0;keep=True
    event="S0-event-71"
    wait=c.mbox('y1', 3*10)
    while i<1000: # simulate work
       i+=1
       if i%500==0:print('Inside Y', i)
       yield
    c.put('x1', "T0-event-25")
    while wait():
        print("Y waiting for event on y1");yield
    else:
        trig=c.get('y1',keep)
        print('Event @Y.y1:', trig)
        if trig==event:
           print('Event happened')
    return

mt=MT(2)
mt.worker(X, ())
mt.worker(Y, ())
mt.start()

