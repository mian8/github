'''
昨天翻硬盘，找到一个好东西，可惜自己加了密码自己不记得了。试了几个常用的没试出来，于是写了这么个小脚本来替我尝试。。呵呵，还真给解出来了。
python脚本内容如下，跑跑自己加密的压缩包还不错

代码如下:
'''
# -*- coding: utf-8 -*-

import sys,os

def IsElementUniq(list):
    """
          判断list中的元素是否为唯一的
    """
    for word in list:
        if list.count(word)&gt;1:
            return False

    return True

def GenPswList():
    """
          要求用户输入词，并根据单词组合密码，只尝试四个单词来组合，并限制密码长度为20。写的比较挫
    """
    psw=raw_input('input a word&gt;')
    wordlist = []
    while psw:
        wordlist.append(psw)
        psw=raw_input('input a word&gt;')
    print wordlist

    global g_pswlist
    g_pswlist = []
    for word in wordlist:
        g_pswlist.append(word)

    for word1 in wordlist:
        for word2 in wordlist:
            locallist = [word1, word2]
            if IsElementUniq(locallist):
                tmp = word1 + word2
                if len(tmp) &lt; 20:
                    g_pswlist.append(tmp)

    for word1 in wordlist:
        for word2 in wordlist:
            for word3 in wordlist:
                locallist = [word1, word2, word3]
                if IsElementUniq(locallist):
                    tmp = word1 + word2 + word3
                    if len(tmp) &lt; 20:
                        g_pswlist.append(tmp)

    for word1 in wordlist:
        for word2 in wordlist:
            for word3 in wordlist:
                for word4 in wordlist:
                    locallist = [word1, word2, word3, word4]
                    if IsElementUniq(locallist):
                        tmp = word1 + word2 + word3 + word4
                        if len(tmp) &lt; 20:
                            g_pswlist.append(tmp)

    print 'gen psw is:', g_pswlist

def TestUnZipPack(filename):
    """
          尝试用密码来解压压缩包
    """

    command = ""
    for psw in g_pswlist:
        command = "7z e -p%s -y %s" %(psw,filename)
        print command
        ret = os.system(command)
        if ret == 0:
            print 'right psw is ', psw
            break

def main(filename):
    GenPswList()
    TestUnZipPack(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'argv error'
        print 'example:test_7z_psw.py 1.7z'
        sys.exit(1)

    main(sys.argv[1])