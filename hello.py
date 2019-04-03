#!/usr/bin/python
#coding=utf-8
import keyword
print ("Hello World");
print ("你好，世界");

print(keyword.kwlist)

#行与缩进
if True:
    print ("True")
else:
    print ("False")

#多行语句

item_one="onr"
item_two="two"
item_three="three"

total = item_one + \
        item_two + \
        item_three

print(total)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

#prin输出

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


print('path:',sys.path)



