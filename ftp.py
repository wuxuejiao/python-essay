__author__ = 'dacxu'  
__mail__ = 'xudacheng06.com'  
__date__ = '2013-10-29'  
__version = 1.0  
  
import sys  
import os  
import json  
from ftplib import FTP  
  
_XFER_FILE = 'FILE'  
_XFER_DIR = 'DIR'  
  
class Xfer(object):  
    ''''' 
    @note: upload local file or dirs recursively to ftp server 
    '''  
    def __init__(self):  
        self.ftp = None  
      
    def __del__(self):  
        pass  
      
    def setFtpParams(self, ip, uname, pwd, port = 21, timeout = 600):          
        self.ip = ip  
        self.uname = uname  
        self.pwd = pwd  
        self.port = port  
        self.timeout = timeout  
      
    def initEnv(self):  
        if self.ftp is None:  
            self.ftp = FTP()  
            print '### connect ftp server: %s ...'%self.ip  
            self.ftp.connect(self.ip, self.port, self.timeout)  
            self.ftp.login(self.uname, self.pwd)   
            print self.ftp.getwelcome()  
      
    def clearEnv(self):  
        if self.ftp:  
            self.ftp.close()  
            print '### disconnect ftp server: %s!'%self.ip   
            self.ftp = None  
      
    def uploadDir(self, localdir='./', remotedir='./'):  
        if not os.path.isdir(localdir):    
            return  
        self.ftp.cwd(remotedir)   
        for file in os.listdir(localdir):  
            src = os.path.join(localdir, file)  
            if os.path.isfile(src):  
                self.uploadFile(src, file)  
            elif os.path.isdir(src):  
                try:    
                    self.ftp.mkd(file)    
                except:    
                    sys.stderr.write('the dir is exists %s'%file)  
                self.uploadDir(src, file)  
        self.ftp.cwd('..')  
      
    def uploadFile(self, localpath, remotepath='./'):  
        if not os.path.isfile(localpath):    
            return
        print '+++ upload %s to %s:%s'%(localpath, self.ip, remotepath)
        global i
        i=i+1
        print i 
        self.ftp.storbinary('STOR ' + remotepath, open(localpath, 'rb'))  
      
    def __filetype(self, src):  
        if os.path.isfile(src):  
            index = src.rfind('\\')  
            if index == -1:  
                index = src.rfind('/')                  
            return _XFER_FILE, src[index+1:]  
        elif os.path.isdir(src):  
            return _XFER_DIR, ''          
      
    def upload(self, src):  
        filetype, filename = self.__filetype(src)  
          
        self.initEnv()  
        if filetype == _XFER_DIR:  
            self.srcDir = src              
            self.uploadDir(self.srcDir)  
        elif filetype == _XFER_FILE:  
            self.uploadFile(src, filename)  
        self.clearEnv()   
                 
  
if __name__ == '__main__':
    i=0
    srcDir = r"c:\ftp\av"  
 #   srcFile = r'E:\1\1.txt'  
    xfer = Xfer()  
    xfer.setFtpParams('172.24.209.108', 'a', 'a')
    a=1
    while a==1:
        xfer.upload(srcDir)      
   # xfer.upload(srcFile)  
