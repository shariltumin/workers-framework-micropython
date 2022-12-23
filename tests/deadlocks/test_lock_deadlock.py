
from worker import task, MT
@task
def test_lock(p):
    n,l1,l2,c,w=p
    s=yield
    while not s.lock(l1, 'XXXX'):
        yield
    else:
        # Critical region
        print(n, 'locking', l1)
        print(n, 'trying to get', l2)
        yield # this will create deadlock
        while not s.lock(l2, 'XXXX'):
           while w>0:
               print(c, end='')
               yield
               w-=1
           print()
           print(n, 'giving up on getting', l2)
           break
        else:
           print(n, 'locking', l2)
           print(n, 'in', l1, 'and', l2)
           print(n, 'leaving.')
           s.unlock(l2, 'XXXX')
        s.unlock(l1, 'XXXX')

mt=MT(2)
mt.worker(test_lock, ('ONE', 'L1', 'L2', '-', 5))
mt.worker(test_lock, ('TWO', 'L2', 'L1', '+', 5))
mt.start()

