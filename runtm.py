#!/lnpp/py37/bin/python3

import sys
import os
from master import smalltool

@smalltool.cpu_runtime
def cmd_runtime(cmd):
    try:
        os.system(cmd)
    except OSError as e:
        print(e)

total = len(sys.argv)
i=1

runtm_list = []

while i<total:
    tm = cmd_runtime(sys.argv[i])
    runtm_list.append([sys.argv[i], tm[0], tm[1]])
    i+=1

for r in runtm_list:
    print("%s : %f s"%(r[0], r[1]))

