import ipdb
import sys


class MyClass:
    "A simple example class"
    i = 12345
    def __init__(self):
        print(sys._getframe().f_code.co_name)
        ipdb.set_trace()
        
    def f(self):
        return 'hello world'
    
if __name__ == '__main__':
    cc = MyClass()
    