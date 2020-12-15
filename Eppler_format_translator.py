# -*- coding: utf-8 -*-
'''
@Time    : 2020/12/14 17:04
@Author  : Junfei Sun
@Email   : sjf2002@sohu.com
@File    : Eppler_format_translator.py
'''

def eppler_printer(newcounter,coordinate):
    for cord in coordinate:
        newcounter += 1
        if newcounter % 8 == 0:
            newf.write(cord)
            newf.write('\n')
        else:
            if cord[0]=='-':
                newf.write(cord)
                newf.write(' ')
            else:
                newf.write(cord)
                newf.write('  ')
    newf.write('\n')

file_name=input('Please input the file name')
f=open(file_name,'r')
data=f.readlines()
lines=0
for line in data:
    lines+=1

xu_coordinate=[]
yu_coordinate=[]
xl_coordinate=[]
yl_coordinate=[]

counter=0
for line in data:
    counter+=1
    line.strip()
    x_c=line.split(' ')[0]
    y_c=line.split(' ')[2].replace('\n','').replace('\n','')
    if counter<lines/2:
        xu_coordinate.append(x_c)
        yu_coordinate.append(y_c)
    else:
        xl_coordinate.append(x_c)
        yl_coordinate.append(y_c)

xu_coordinate.reverse()
yu_coordinate.reverse()

print('upper surface x_coordinate:',xu_coordinate)
print('upper surface y_coordinate:',yu_coordinate)
print('lower surface x_coordinate:',xl_coordinate)
print('lower surface y_coordinate:',yl_coordinate)

new_file_name=input('please input the new file name')

newf=open(new_file_name,'a')
newcounter=0
eppler_printer(newcounter,xu_coordinate)

newcounter=0
eppler_printer(newcounter,yu_coordinate)

newcounter=0
eppler_printer(newcounter,xl_coordinate)

newcounter=0
eppler_printer(newcounter,yl_coordinate)

newf.close()
f.close()