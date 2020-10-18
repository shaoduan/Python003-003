#!/usr/bin/env python3

#自定义一个 python 函数，实现 map() 函数的功能。

def mymap(func, *args):
    lenths = [ len(i) for i in args ]
    vars = []
    for idx in range(min(lenths)):
        for arg in args:
            vars.append(arg[idx])
        yield func(*vars)