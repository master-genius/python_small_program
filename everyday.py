

import os
import subprocess
import time

i=0
upd_flag=0;
while 1:
    time.sleep(300)
    tm=time.localtime()
    print("%d.%d.%d %d:%d:%d Checking for permission to update deposit"%\
        (tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec))
    if tm.tm_hour!=1:
        upd_flag=0
        continue
    elif upd_flag>0:
        continue
    try:
        i+=1
        print("update balance %d"%(i))
        subprocess.call('D:\\phpStudy2016\\php\\php-7.1.3-nts\\php.exe D:\\work\\3000\\everyday_interest.php')
        upd_flag=1
    except subprocess.CalledProcessError as e:
        print(e)
        
    