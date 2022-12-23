

# test_wait_signal_deadlock.py
from worker import task, MT
from random import random

@task
def X(pm):
  c=yield; i=0; keep=True
  event="T0-event-25"
  wait=c.mbox('x1',50)
  while wait():
      i+=1
      if i%10000==0:
         print("X waiting for event on x1", i)
      yield
  else:
      ev=c.get('x1', keep)
      print("X get", ev)
      if ev==event:
         print('Event @X:', c.get('x1'))
         c.put('y1', "S0-event-31")
  return

@task
def Y(pm):
    c=yield;i=0;keep=True
    event="S0-event-31"
    wait=c.mbox('y1',50)
    while wait():
        i+=1
        if i%10000==0:
           print("Y waiting for event on y1", i)
        yield
    else:
        ev=c.get('y1', keep)
        print("Y get", ev)
        if ev==event:
           print('Event @Y:', c.get('y1'))
           c.put('z1', "R0-event-13")
    return

@task
def Z(pm):
    c=yield;i=0;keep=True
    event="R0-event-13"
    wait=c.mbox('z1',50)
    while wait():
        i+=1
        if i%10000==0:
           print("Z waiting for event on z1", i)
        yield
    else:
        ev=c.get('z1', keep)
        print("Z get", ev)
        if ev==event:
           print('Event @Z:', c.get('z1'))
           c.put('x1', "T0-event-25")
    return

@task
def H(pm):
    c=yield
    w=int((random()*10)+1)%3
    if w==0:
       c.put('y1', "S0-event-31")
    elif w==1:
       c.put('z1', "R0-event-13")
    else:
       c.put('x1', "T0-event-25")
    return

mt=MT(4)
mt.worker(X, ())
mt.worker(Y, ())
mt.worker(Z, ())
mt.worker(H, ())
mt.start()
print(mt.log())

