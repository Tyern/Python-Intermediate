import logging
import time
from functools import wraps

class wrapper:
    def __init__(self, org_func):
        self.org_func = org_func
        logging.basicConfig(filename=f'{org_func.__name__}.log', level=logging.INFO)

    def __call__(self, *args, **kwargs):
        # self.__call__ = wraps(self.org_func)(self.__call__)
        logging.info(f'the function {self.org_func.__name__} is run with {args}, {kwargs}')
        return self.org_func(*args, **kwargs)

# handle the error made by class is way harder than using function

def higher_deco_func(PREFIX): # another nest function to add more decorator to the main func
    def wrapper_deco(org_func):
        logging.basicConfig(filename=f'{org_func.__name__}.log', level= logging.INFO)
        @wraps(org_func)
        def log_config(*args, **kwargs):
            logging.info(f'the function {org_func.__name__} is run with {args}, {kwargs}')
            print(f'{PREFIX:-^75}')
            return org_func(*args, **kwargs)
        return log_config
    return wrapper_deco

def cal_process_time(org_func):
    @wraps(org_func)
    def main_func(*args, **kwargs):
        t1 = time.process_time()
        result = org_func(*args, *kwargs)
        t2 = time.process_time()
        print(f'[process time {t2 - t1:.3f}]')
        return result
    return main_func

@higher_deco_func('*****')
# @wrapper
@cal_process_time
def myfunc(arr):
    '''find the average value of the array'''
    length = 0
    s = 0
    for i in arr:
        length += 1
        s += i
    assert length > 0, ' the array should not have length 0'
    return s / i

print(myfunc(range(10000000)))