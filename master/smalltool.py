
import time
import platform
import os

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

def time_loop():
    week_map = {
        'w0':'星期一',
        'w1':'星期二',
        'w2':'星期三',
        'w3':'星期四',
        'w4':'星期五',
        'w5':'星期六',
        'w6':'星期日'
    }
    try:
        clear_ins = 'clear'
        if is_windows():
            clear_ins = 'cls'
        while True:
            t = time.localtime()
            print("%d:%d:%d %s'%d-%d-%d"%(t.tm_hour,t.tm_min,t.tm_sec,week_map['w'+str(t.tm_wday)],t.tm_year,t.tm_mon,t.tm_mday))
            time.sleep(1)
            os.system(clear_ins)
    except OSError as e:
        print(e)
    except KeyboardInterrupt:
        print("bey!\n")

