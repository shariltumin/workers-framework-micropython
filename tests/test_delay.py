
from worker import task, MT

@task
def test_delay(p):
    n,w=p
    print(f'{n} start')
    s=yield
    wait=s.delay(w)
    while wait():
       yield
    print(f'{n} stop')

mt=MT(3)
mt.worker(test_delay, ('ONE', 10))
mt.worker(test_delay, ('TWO', 6))
mt.worker(test_delay, ('THREE', 3))
mt.start()

