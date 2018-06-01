from collections import deque
import ipdb
import time


def countdown(n):
    while n > 0:
        print('T-minus',n)
        time.sleep(1)
        yield n
        n -= 1
    print('Blastoff!')
    
def countup(n):
    x = 0
    while x < n:
        time.sleep(2)
        print('Counting up',x)
        yield
        x += 1
        
class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()
        
    def new_task(self,task):
        self._task_queue.append(task)
        
    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                print(next(task))
                self._task_queue.append(task)
            except StopIteration:
                pass

def jump_range(up_to):
    kk = 0
    while kk < up_to:
        ipdb.set_trace()
        yy = yield kk    #yield就是每个生成器产生数据的位置，并记住这个位置，下一次迭代继续从这里开始
        # ipdb.set_trace()
        print("yy",yy,end=';')
        # ipdb.set_trace()
        if yy is None:
            yy = 1
        kk += yy
        # ipdb.set_trace()
        print("kk", kk,end=';')
        
# import itertools
# 迭代器切片  itertools.islice(iter,10,20)  iter为某个需要切片的迭代器
# 反向迭代 reversed()
#
        

if __name__ == '__main__':
    sched = TaskScheduler()
    sched.new_task(countdown(10))
    sched.new_task(countdown(5))
    sched.new_task(countup(15))
    sched.run()
    # #send传递参数给yield表达式，这是传递的参数回座位表达式的值，即强行修改了上一个yield位置产生的值
    # iterator = jump_range(10)
    # print(next(iterator))     #生成第一个数据0，这时程序跑到了第一次yield的位置
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print('haha')
    # print(iterator.send(4))   #这时将yield的值强行修改为了4
    # print(next(iterator))     #这时程序开始往下跑，经过基于
    # print(iterator.send(-1))