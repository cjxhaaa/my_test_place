from collections import deque
from functools import wraps
import gevent
from gevent import monkey
from functools import partial
import asyncio
import random
import twisted
import requests
import time

monkey.patch_socket()
session = requests.Session()

urls = [
    'http://www.cjxh616.com',
    'https://cn.pharmacyonline.com.au/1064714.html',
    'https://cn.pharmacyonline.com.au/1064715.html',
    'https://cn.pharmacyonline.com.au/1064712.html'
]

new_urls = (url for url in urls)

class Timer():
    def __init__(self,name):
        self.name = name
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print("{} use {}".format(self.name,self.end-self.start))


def print_time(name=None):
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args,**kwargs):
            if name:
                time_name = name
            else:
                time_name = args[0]
            with Timer(time_name):
                return func(*args,**kwargs)
        return wrapper2
    return wrapper1

class TaskScheduler():
    def __init__(self,work):
        self._task = deque()
        self._work = work
    
    def add_task(self,task):
        self._task.append(task)
        
    def run(self):
        while self._task:
            task = self._task.popleft()
            try:
                url = next(task)
                response = next(self._work(url))
                import ipdb
                ipdb.set_trace()
                self.add_task(task)
            except StopIteration:
                pass

    
@print_time()
def request(url):
    return session.request('GET',url)


    

async def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        await asyncio.sleep(1)
        print('smart one think 1 secs to get {}'.format(b))
        a, b = b, a+b
        index += 1
        
        
        
async def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        await asyncio.sleep(2)
        print('stupid one think 2 secs to get {}'.format(b))
        a, b = b, a+b
        index += 1
        
from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = { }          # Mapping of names to actors
        self._msg_queue = deque()   # Message queue

    def new_actor(self, name, actor):
        '''
        Admit a newly started actor to the scheduler and give it a name
        '''
        self._msg_queue.append((actor,None))
        self._actors[name] = actor

    def send(self, name, msg):
        '''
        Send a message to a named actor
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))

    def run(self):
        '''
        Run as long as there are pending messages.
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                 actor.send(msg)
            except StopIteration:
                 pass

# Example use
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)

    def counter(sched):
        while True:
            # Receive the current count
            n = yield
            if n == 0:
                break
            # Send to the printer task
            sched.send('printer', n)
            # Send the next count to the counter task (recursive)

            sched.send('counter', n-1)

    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    # Send an initial message to the counter to initiate
    sched.send('counter', 10)
    sched.run()

#
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # tasks = [
#     #     # asyncio.async(smart_fib(10)),
#     #     # asyncio.async(stupid_fib(10)),
#     # ]
#     # loop.run_until_complete(asyncio.wait(tasks))
#     # print('All finishe')
#     # loop.close()
#     with Timer('123'):
#         jobs = [gevent.spawn(request,url) for url in urls]
#         gevent.joinall(jobs)
#     # scheduler = TaskScheduler(request)
#     # scheduler.add_task(new_urls)
#     # scheduler.run()