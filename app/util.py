# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True


def create_dir_if_not_exist(dir_path):
    import os
    if not os.path.exists(dir_path):
        print 'creating path:', dir_path
        os.mkdir(dir_path)