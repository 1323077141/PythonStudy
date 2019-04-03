#!/usr/bin/python3


counter=100
miles=1000.0
name="runoob"

print(counter)
print(miles)
print(name)

#多个变量赋值
a=b = c = 1
a,b,c=1,2,"runoob"

#数据类型由6个：Number(数字);String(字符串);List(列表);Tuple(元组);Set(集合);Dictionary(字典)
'''
不可变数据:Number,String,Tuple
可变数据：List,Dictionary,Set
'''
#Number:int,float,bool,complex
a,b,c,d=20,5.5,True,4+3j
print("type:",type(a),type(b),type(c),type(d))
print("isinstance:",isinstance(a,int))

#数值运算：+,-,*,/(浮点数),//(得到整数),%,**(乘方)

#String:' 或者"引号内,\可表示转义字符:变量[头下标:尾下标]

str = 'Runoob'
 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

#Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')
print(r'Ru\noob')

#索引值以 0 为开始值，-1 为从末尾的开始位置。
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


#集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print(a - b)     # a 和 b 的差集
 
print(a | b)     # a 和 b 的并集
 
print(a & b)     # a 和 b 的交集
 
print(a ^ b)     # a 和 b 中不同时存在的元素

#Dictionary 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。 键(key)必须使用不可变类型,在同一个字典中，键(key)必须是唯一的。

dict = {}
dict['one'] = "1 - value1"
dict[2]     = "2 - value2"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#构造函数 dict() 可以直接从键值对序列中构建字典如下：
#print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
#print({x: x**2 for x in (2, 4, 6)})
#print(dict(Runoob=1, Google=2, Taobao=3))































