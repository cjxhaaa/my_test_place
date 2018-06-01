import time
from queue import Queue

class TaskScheduler:
    def __init__(self):
        self._task_queue = Queue()
    
    def new_task(self, task):
        self._task_queue.append(task)
    
    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                print(next(task))
                self._task_queue.append(task)
            except StopIteration:
                pass