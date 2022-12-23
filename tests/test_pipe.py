
# test_pipe.py
from worker import task, MT
from pipe import Pipe

@task
def X(pm):
  s=b''
  c=yield; pipe=c.v.pipe
  while True:
     r=pipe.get()
     if len(r)==0: # buffer empty
        yield
     else:
        if len(r)==1 and r==b'\0': # end of message
           break
        else:
           s+=r
     yield
  print(s.decode())
  return

@task
def Y(pm):
    s='One for the money.\nTwo for the show.\n'
    s+='Three to get ready.\nNow go, cat, go.\n'
    c=yield; pipe=c.v.pipe
    i=0
    s=s.encode() # change to bytes
    while i<len(s):
        r=pipe.put(s[i:i+1]) # use subarray. s[i]!=s[i:i+1]
        if r==0:
           yield
        else:
           i+=1
    yield # message end, let comsumer get it first
    while True: # send end of message 1 byte
       r=pipe.put(b'\0')
       if r==0:
          yield
       else:
          return

mt=MT(2)
mt.s.v.pipe=Pipe(1) # 1 byte ring buffer
print('\nring-buffer:', mt.s.v.pipe.a, '\n')
mt.worker(X,())
mt.worker(Y,())
mt.start()
print(mt.log())

