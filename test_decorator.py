import time
from functools import wraps
import ipdb


class Timer():
    def __init__(self,name):
        self.name = name
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('{} use {}s'.format(self.name,self.end-self.start))
        

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        with Timer(func.__name__):
            return func(*args, **kwargs)
    return wrapper

@timer
def gg(x):
    time.sleep(1)
    print(x)


'''
在上面的 wrapper() 函数中，装饰器内部定义了一个使用 *args 和 **kwargs 来接受任意参数的函数。
在这个函数里面调用了原始函数并将其结果返回，不过你还可以添加其他额外的代码(比如计时)。
然后这个新的函数包装器被作为结果返回来代替原始函数。

需要强调的是装饰器并不会修改原始函数的参数签名以及返回值。
使用 *args 和 **kwargs 目的就是确保任何参数都能适用。
而返回结果值基本都是调用原始函数 func(*args, **kwargs) 的返回结果，其中func就是原始函数。
'''

'''
问题：你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。

解决：
任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数。
@wraps 有一个重要特征是它能让你通过属性 __wrapped__ 直接访问被包装函数
__wrapped__ 属性还能让被装饰函数正确暴露底层的参数签名信息
'''

@timethis
def countdown(n):
    while n > 0:
        n -= 1
        
'''
*args和**kwargs的强制参数签名


'''


'''
带参数装饰器
'''
import logging

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        # ipdb.set_trace()
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.CRITICAL,'123','345')
def add(x,y):
    return x+y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    print(add(1,2))
    spam()
    countdown(1000000)