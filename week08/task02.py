#!/usr/bin/env python3

#自定义一个 python 函数，实现 map() 函数的功能。

def mymap(func, *args):
    lenths = [len(i) for i in args]
    for idx in range(min(lenths)):
        vars = []
        for arg in args:
            vars.append(arg[idx])
        yield func(*vars)


def mymap2(func, *args):
    for func_args in zip(*args):
        yield func(*func_args)