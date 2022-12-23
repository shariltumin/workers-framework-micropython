# Beware of deadlocks

Deadlock is any situation in concurrent computing in which no tasks can proceed because each is waiting for another task, including itself, to take action,
such as sending a message or, more commonly, releasing a lock.

Each task, however, is blocking other tasks by holding a critical resource.
One solution is to release critical resources after a predetermined timeout.
