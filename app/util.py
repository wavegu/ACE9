# encoding=utf8
import re
import urllib2
import sys
import socket
import fcntl
import struct
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


def get_ip_address():

    def visit(url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            s = opener.read()
            asd = re.search('\d+\.\d+\.\d+\.\d+', s).group(0)
            return asd

    try:
        myip = visit("http://www.whereismyip.com/")
        print 1
        print myip
        return myip
    except:
        print 2
        try:
            myip = visit("http://www.bliao.com/ip.phtml")
            print myip
            return myip
        except:
            print 3
            try:
                myip = visit("http://www.ip138.com/ip2city.asp")
                print myip
                return myip
            except:
                myip = "So sorry!!!"
    return myip


def create_dir_if_not_exist(dir_path):
    import os
    if not os.path.exists(dir_path):
        print 'creating path:', dir_path
        os.mkdir(dir_path)
