# -*- coding: utf-8 -*-
'''
@Time    : 2020/12/27 15:31
@Author  : Junfei Sun
@Email   : sjf2002@sohu.com
@File    : Selig_format_translator.py
'''

file_name=input('Please input the file name')
f=open(file_name,'r')
data=f.readlines()
f.close()

newfile_name=input('Please input the new file name')
fw=open(newfile_name,'a')
counter=0
for line in data:
    counter+=1
    line = line.strip()
    line = line.strip('\n')
    if counter>=4:    #changeable(according to how many redundant lines are covered)
        line = line.split(' ')
        for i in range(line.count('')):
            line.remove('')
        if line[2].find('-')==0:
            newline = ' ' + line[1] + ' ' + line[2]
        else:
            newline=' '+line[1]+'  '+line[2]
        fw.write(newline+'\n')
fw.close()