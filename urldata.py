#!/usr/bin/python3

import os
import sys
from urllib import request as ureq
from urllib import error as urlerror
import time
import platform
import sys
import re

__version__ = '1.0.1'
__info__ = 'Copyright by WangKai 2017.05.04 Free Software. '+\
        'Anyone can use it by free and forbidden to use it in commerial'

try:
    _down_path = ''
    _clear_ins = 'clear'
    plat = platform.platform().lower()
    if 'windows' in plat:
        _down_path = 'D:/py/downloads/'
        _clear_ins='cls'
    else:
        _down_path = os.getenv('HOME')+'/Downloads'
        
    if not os.path.isdir(_down_path):
            os.mkdir(_down_path)
except OSError as e:
    print(e)
    exit(-1)
    
#url = 'http://ftp.sjtu.edu.cn/ubuntu/pool/main/g/gcc-7/gcc-7_7.1.0.orig.tar.gz'

class downurl:
    def __init__(self,url=''):
        self.filename=''
        self.path_file=''
        self.is_continue=0
        self.is_here=0
        self.url=url
        #0:downliading; 1:success; 2:failed;
        self.status=0
        self.filesize=0
        self.down_size=0
        self.start_size=0
        self.show_size=0
        self.show_size_unit = 'B'
        #init download unit
        self.net_unit=102400
        
        self.furl = ureq.FancyURLopener()
        self.furl.addheader('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0")
        #self.furl.addheader('Host',"www.aaa.com")
        #self.furl.addheader('Referer',"https://www.baidu.com")
        #self.furl.version = 'Mozilla/5.0'
        #match html media url
        self.media_match_list = []
        
    def check_file(self,ulength=0):
        if os.path.isfile(self.path_file):
            self.is_here=1
            ft = os.stat(self.path_file)
            if ulength > ft.st_size:
                self.is_continue=1
                self.down_size=ft.st_size
                self.start_size=ft.st_size+1
            else:
                self.status=1
        else:
            self.is_here=0

    def get_header(self,):
        h = self.furl.open(self.url)
        if not h.closed:
            print(h.headers.as_string())
        else:
            print("link closed by server")
        
    def core_download(self,):
        try:
            h = self.furl.open(self.url)
            if h.closed:
                print("ERROR: link closed by server")
                exit(0)
                
            fmode = 'wb+'
            if self.is_continue == 1:
                fmode='ab+'
            fd = open(self.path_file,fmode)
            caclt_show=time.time()
            caclt_count=0
            
            while 1:
                tm = time.time()
                if h.closed:
                    print("ERROR: url closed by server")
                    break
                data = h.read(int(self.net_unit))
                wcount = fd.write(data)
                caclt_count += wcount
                self.down_size += wcount
                if wcount<=0:
                    print("%s success to download."%(self.filename))
                    break
                fd.flush()
                tm_diff = tm-caclt_show
                if tm_diff>=1.0:
                    speed = ((caclt_count*1.0)/tm_diff)/1024
                    if tm_diff > 1.1:
                        self.net_unit = self.net_unit/2
                    os.system(_clear_ins)
                    print("%s  speed:%.2fKb/s  %.2f%%  %.2f%s"%\
                            (self.filename,speed,(self.down_size*100.0)/self.filesize,self.show_size,self.show_size_unit))
                    caclt_count=0
                    caclt_show=tm
                else:
                    if self.net_unit <= 2000000:
                        self.net_unit *= 2
                    else:
                        self.net_unit += 200000
            h.close()
            fd.close()
        except KeyboardInterrupt:
            h.close()
            fd.flush()
            fd.close()
            print("force exit")
            exit(0)

    
    def download(self,url=''):
        if url == '':
            url = self.url
        else:
            self.url=url
            
        try:
            hf = ureq.urlopen(url)
            self.filesize = hf.headers.get('Content-Length')
            if self.filesize is None:
                print("ERROR: file size is illegal")
                exit(-1)

            self.filesize = int(self.filesize)

            if self.filesize > 10000 and self.filesize<=10000000:
                self.show_size = (self.filesize*1.0/1024)
                self.show_size_unit = 'Kb'
            elif self.filesize > 1000000:
                self.show_size = (self.filesize*1.0/(1024*1024))
                self.show_size_unit = 'Mb'

            if '?' in url:
                url = url[0:url.index('?')]
            fname = hf.headers.get('Content-Disposition')
            if fname == '' or fname is None:
                fname = url.strip('/').split('/')[-1]
            else:
                fname = fname.split('filename:')[-1].strip()
                if fname == '':
                    fname = str(time.time())
            
            self.path_file = _down_path + '/'+fname
            self.filename = fname
            hf.close()
            
            print("download file:%s to %s"%(fname,_down_path))
            print("file size:%d"%(self.filesize))
            
            self.check_file(self.filesize)
            if self.is_here==1 and self.status==1:
                print("%s already here. What do you want?"%(self.filename))
                print("1. exit\n2. again download\n3. rename and download")
                ins = input('enter the number_')
                if ins == '1':
                    exit(0)
                elif ins == '2':
                    print("start to rebuild download...")
                elif ins == '3':
                    self.filename = str(time.time())+'-'+self.filename
                    self.path_file = _down_path+self.filename
                else:
                    exit(0)
            elif self.is_here==1 and self.status==0:
                self.furl.addheader('range','bytes=%d-%d'%(self.start_size,self.filesize))
                print("continue download the file: %s"%(self.filename))
                print("start size: %d"%(self.start_size))
                
            self.core_download()
        except urlerror.URLError as e:
            print(e)
            exit(-1)
        except IOError as e:
            print(e)
            exit(-1)
        except SystemExit as e:
            if e.code!=0:
                print("abrot code:%d"%(e.code))
            exit(-1)
        except ValueError as e:
            print(e)
            exit(-1)


#--------------  end the class ------------------------------#            

def dhelp():
    help_info = 'urldata help doc \n\nusage: urldata [options] url\n'+\
        'if you ignore the arguments , the program output the help info.\n'+\
        'if the argument is a file path , the program will read the file as a link list.\n'+\
        '--header          -h   print url header\n'+\
        'example: python3 py/urldata.py "http://www.abc.com/aaa.zip"\n'
    print(help_info)


if __name__ == '__main__':
    args_len = len(sys.argv)
    if args_len<2:
        print("less arguments: file with a url and [options]")
        dhelp()
    elif args_len==2:
        a = sys.argv[1]
        du = downurl(a)
        #du.get_header()
        du.download()
    else:
        url_func = 'download()'
        url=''
        url_regex = 'http|ftp://.*'
        for i in range(1,args_len):
            if sys.argv[i] == '--header' or sys.argv[i] == '-h':
                url_func = 'get_header()'
            else:
                if re.match(url_regex,sys.argv[i]):
                    url = sys.argv[i]
                else:
                    print("%s is not seem a right url and it is not a right argument,please check your input"%\
                        (sys.argv[i]))
                    exit(-1)
        if url == '':
            print("Please enter the right url")
            exit('-1')
        drun = 'downurl(url).%s'%(url_func)
        print("run:%s"%(drun))
        exec(drun)
