#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
while 1:
    s_ = int(random.uniform(1, 3))
    s = str(s_)
    m = raw_input('输入 1（石头）、2（剪子）、3（布）,输入"end"结束游戏:')
    alist = ["石头","剪刀","布"]
    blist = ["1","2","3"]
    if (m not in blist) and (m != 'end'):
        print "输入错误，请重新输入！"
    elif (m not in blist) and (m == 'end'):
        print "\n游戏退出中..."
        break
    elif m == s :
        print "电脑出了： " + s+"("+alist[s_-1]+")"+  "，平局！"
    elif (m == '1' and s =='2') or (m == '2' and s =='3') or (m == '3' and s =='1'):
        print "电脑出了： " + s+"("+alist[s_-1]+")"+ "，你赢了！"
    elif (m == '1' and s =='3') or (m == '2' and s =='1') or (m == '3' and s =='2'):
        print "电脑出了： " + s+"("+alist[s_-1]+")"+ "，你输了！"
    else :
        print "m:"+m+"   s:"+s
        print "未知错误！"