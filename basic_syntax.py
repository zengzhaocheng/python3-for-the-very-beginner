'''
#源文件字符编码的改变，没搞懂，报错SyntaxError: encoding problem: cp-1252

#######  !/usr/bin/python3
第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。

此外还有以下形式（推荐写法）：
#!/usr/bin/env python3
这种用法先在 env（环境变量）设置里查找
 python 的安装路径，
 再调用对应路径下的解释器程序完成操作。

'''

import keyword
import io
import sys
#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
print(keyword.kwlist)

#注释0

'''

注释1
'''

"""
注释2

"""

#行与缩进：用缩进来表示代码块而不是{}
#缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

if True:
    print("true")
else:
    print("false")
  #print("haha")
  #报错IndentationError

#多行语句，python通常是一行写完一条语句
#但是如果语句很长，我们可以用反斜杠\来实现多行语句

total = 1 + 2 + 4 \
    + 5 + 1 + \
        + 11

print(total)
#在[] {} ()中的多行语句，不需要使用\
total = ['item_one',
'item_two', 'item_three', 'item_four'
, 'item_five'
]
print(total)

#数字（NUMBER）类型
#int bool float complex
a = 1
b = True
c = 1.23
d = 3e-2
e = 1 + 2j
print("type of a is:",type(a))
print("type of b is:",type(b))
print("type of c is:",type(c))
print("type of d is:",type(d))
print("type of e is:",type(e))

#字符串（string）：''' 三引号可以指定一个多行字符串
word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以由多行组成"""
str = '123456789'
print(str)  #输出str
print(str[0:-1]) #输出第一个到倒数第 二 个的所有字符
print(str[0]) 
print(str[2:5])
print(str[2:]) #第三个以后
print(str[1:5:2]) #输出第二个到第五个，以2为步长
print(str*2)   #输出字符串两次
print(str+'你好')  #连接字符串  无法输出中文？

print('------------------------------')

print('hello\nyu')  #使用反斜杠 \n 表示回车
print(r'hello\nyu') # 在字符串前面加上r(raw)，表示原始字符串，不会发生转义



#等待用户输入

input("\n\n 按下 enter键后推出。")

#同一行显示多条语句 用 ; 隔开

import sys; x = 'y';sys.stdout.write(x + '\n')

#多个语句构成代码组 if else while def class

if True:
    print("haha")
elif True:
    print("hehe")
else :
    print("hihi")

#print 输出默认换行，如果要实现不换行需要在变量末尾加上 end = ""

x = "a"
y = "b"
print(x)
print(y)

print('-----------')

#不换行
print(x, end = " ")
print(y, end = " ")
print()

#import somemodule和 from somemodule import somefunction1, somefunction2 ;from s import *
import sys
print("命令行参数：")
for i in sys.argv:
    print(i)
print('-------------------')
print('\n python 路径为', sys.path)

from sys import argv,path
print('-------------------')
print('path',path) #因为已经导入sys的path 所以不用加sys.path
print('---------------------')


#命令行参数python -h 查看个参数