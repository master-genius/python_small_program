
import time
import platform

def cpu_runtime(func):
    def wrapper(*args):
        start_clock = time.clock()
        start_time = time.time()
        func(*args)
        end_clock = time.clock()
        end_time = time.time()
        return ((end_time - start_time),(end_clock - start_clock))
    return wrapper

def fibonacc(n):
    a=0
    b=1
    for i in range(0,n):
        a,b = b,a+b
        yield b

def what_system():
    plat = platform.platform().lower()
    if 'windows' in plat:
        return 'win'
    elif 'linux' in plat:
        return 'linux'
    elif 'unix' in plat or 'bsd' in plat:
        return 'unix'
    else:
        return 'unknow'

def is_linux():
    if what_system() == 'linux':
        return 1
    else:
        return 0

def is_windows():
    if what_system() == 'win':
        return 1
    else:
        return 0

