
from worker import task, MT
from random import random
@task
def test_lock(p):
    n,l1,l2,c,w=p
    s=yield
    while not s.lock(l1, n):
        yield
    else:
        # Critical region
        print(n, 'locking', l1)
        print(n, 'trying to get', l2)
        yield # this will create deadlock
        while not s.lock(l2, n):
           while w>0:
               print(c, end='')
               yield
               w-=1
           print()
           print(n, 'giving up on getting', l2)
           print(n, 'releasing', l1)
           s.unlock(l1, n)
           w=int((random()*10)+1)
           while w>0: yield; w-=1
           mt.worker(test_lock, p)
           return
        else:
           print(n, 'locking', l2)
           print(n, 'in', l1, 'and', l2)
           print(n, 'leaving.')
           s.unlock(l2, n)
        s.unlock(l1, n)

mt=MT(4)
mt.worker(test_lock, ('ONE', 'L1', 'L2', '-', 5))
mt.worker(test_lock, ('TWO', 'L2', 'L1', '+', 5))
mt.start()

