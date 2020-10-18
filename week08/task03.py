#!/usr/bin/env python3
import time
from functools import wraps


def timer(func):
    '''
    实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
    '''
    #@wraps(func)
    def wrapper(*args, **kargs):
        start_time = time.time()
        ret = func(*args, **kargs)
        end_time = time.time()
        elapse = end_time - start_time
        print(f'Function: {func.__name__} Run {elapse}')
        return ret
    return wrapper

@timer
def func(*args, **kargs):
    print(f'func.name: {func.__name__}')
    time.sleep(2)
    return args, kargs


# Test Case
print(func(1,2,3,c=1,b=2))