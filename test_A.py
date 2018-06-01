#!/usr/bin/env python
from __future__ import print_function


# class A():
#     def __init__(self):
#         getattr(self, "out")()
#
#     def out(self):
#
#         A = "ok"
#
#         def _inner():
#
#             if A.lower() == "ok":
#
#                 print("ok")
#
#                 A = 2
#
#             print("inner print A", A)
#
#         _inner()
#         print("outter print A", A)
#
#
# A()

x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        # global x
        
        print("inner:", x)
        x = 2

    inner()
    print("outer:", x)

outer()
print("global:", x)

# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)