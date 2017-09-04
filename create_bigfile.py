#!/usr/bin/python3

import os
from master import smalltool
import random

def rand_text(length = 50):
    text_str = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text_end = len(text_str) - 1
    text = ''
    for i in range(0,length-1):
        text += text_str[random.randint(0,text_end)]
    return text


def create_bigf():
    try:
        file_dir = os.getenv("HOME") + '/tmp'
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)
        file_path = file_dir + '/big_file.test'
        fd = open(file_path,'w+')
        for i in range(0,100000):
            text = rand_text(random.randint(49,128))
            fd.write(text+"\n")
        fd.flush()
        fd.close()
    except OSError as e:
        print(e)
    except IOError as e:
        print(e)
    except:
        print("Error:unkow error")

create_bigf()

