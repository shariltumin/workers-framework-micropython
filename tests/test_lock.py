
from worker import task, MT

def critical_region(n):
    print(f'{n} in critical region')

@task
def test_lock(p):
    n,l,w=p
    s=yield
    while not s.lock(l, 'XXXX'):
        yield
    else:
        # Critical region
        critical_region(n)
        wait=s.delay(w)
        while wait():
            yield
        s.unlock(l, 'XXXX')

mt=MT(2)
mt.worker(test_lock, ('ONE', 'L', 5))
mt.worker(test_lock, ('TWO', 'L', 5))
mt.start()

