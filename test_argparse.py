import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square",type=int,help="display a square of a given number")
# parser.add_argument("-v","--verbosity",action="count",default=0,help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
#
# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(args.square,answer))
# elif args.verbosity == 1:
#     print("{}^ == {}".format(args.square,answer))
# else:
#     print(answer)


# parser = argparse.ArgumentParser()
# parser.add_argument("x",type=int,help="the base")
# parser.add_argument("y",type=int,help="the exponent")
# parser.add_argument("-v","--verbosity",action="count",default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# if args.verbosity >= 2:
#     # print("{} to the power {} equals {}".format(args.x,args.y,answer))
#     print("Running '{}'".format(__file__))
# if args.verbosity >= 1:
#     print("{}^{} == ".format(args.x,args.y,),end="aaaa") #end不会换行
# print(answer)


# parser = argparse.ArgumentParser(description="calculatte X to the power of Y")
# # add_mutually_exclusive_group()添加互斥参数，参数无法同时存在
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v","--verbose",action="store_true")
# group.add_argument("-q","--quiet",action="store_true")
# parser.add_argument("x",help="the base")
# parser.add_argument("y",help="the exponent")
# args = parser.parse_args()
# answer = args.x+args.y
#
# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print("{} to the power {} equals {}".format(args.x,args.y,answer))
# else:
#     print("{}^{} == {}".format(args.x,args.y,answer))

# action 参数动作
# store保存参数值，默认动作
# store_const保存一个呗定义为参数规格一部分的值，而不是一个来自参数解析而来的值，这通常用于实现非布尔值的命令行标记
# store_true/store_false保存响应的布尔值。这两个动作被用于实现布尔开关。
# append将值保存到一个列表中。若参数重复出现，则保存多个值。
# append_const将一个定义在参数规格中的值保存到一个列表中。
# version打印光宇程序的版本信息，然后退出

parser = argparse.ArgumentParser()

parser.add_argument("x",help="the base")

subparsers = parser.add_subparsers(help='commands')

# A list command
list_parser = subparsers.add_parser('list', help='List contents')
list_parser.add_argument('dirname', action='store', help='Directory to list')

# A create command
create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument('dirname', action='store', help='New directory to create')
create_parser.add_argument('--read-only', default=False, action='store_true',
        help='Set permissions to prevent writing to the directory')

# A delete command
delete_parser = subparsers.add_parser('delete', help='Remove a directory')
delete_parser.add_argument('dirname', action='store', help='The directory to remove')
delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
        help='Remove the contents of the directory, too')

print(parser.parse_args())