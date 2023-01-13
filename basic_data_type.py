#python 变量不需要声明每个变量使用前必须赋值，赋值之后才会被创建
#在python 中，变量就是变量，它没有类型，但一个变量可以通过赋值指向不同类型的变量
#所谓的类型，指的是变量所指的内存中对象的类型


a = b = c = 1 #允许多变量赋值，从后向前赋值
print(a," ",b," ",c)
a, b, c = 1, 2, 'runoob'
print(a," ",b," ",c)

#标准数据类型(六种)：
# 不可变数据：Number, String, Tuple
#  可变数据： List,  Set, Dictionary


#判断类型
print(type(a),type(c))
#or
print(isinstance(a,int))
#type 和 isinstance 的区别在于：
# type不会认为子类是一种父类类型，而isinstance会

class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))#True
print(type(A())==A)     #True
print(isinstance(B(),A))#True
print(type(B())==A)     #False


#python3中 bool是int的子类 可以用is判断

print(issubclass(bool,int)) #True 无法判断 
print(True+1)
print(False+1)
print(False == 0)
print(1 is True)
print(0 is False) #False 可以判断 


#当你指定一个值时，对象就会被创建
var1 = 1
var2 = 10
#也可以用del语句删除一些对象引用
del var1,var2
#+-*/
print(1+1," ",4.3-2," ",3*8,2/4,2//4,17%3,2**5)#依次是加减乘除，除向下取整，取余，乘方
#混合计算会转换成浮点
#复数a+bj 或者 complex(a,b) a,b 都是浮点型

#字符串

str = '123456789'
print(str)  #输出str
print(str[0:-1]) #输出第一个到倒数第 二 个的所有字符
print(str[0]) 
print(str[2:5])##索引和截取的下标不一样
print(str[2:]) #第三个以后
print(str[1:5:2]) #输出第二个到第五个，以2为步长
print(str*2)   #输出字符串两次 用*重复
print(str+'你好')  #连接字符串 无法输出中文修改系统环境变量 
print(str[-1])#最后一个字符，从右往左-1开始，-2,-3...

#python中的字符串不能改变


#List: 卸载方括号之间，元素用逗号隔开，元素可以改变。

#List 索引和截取和字符串类似，+表示连接，*表示重复

list = ['abcd',789,2.23,'yu',80]
tinylist = [123,'z']
print(list)
print(list[0])
print(list[1:3])
print(list[2])
print(list[2:])
print(tinylist*2)
print(list + tinylist)

print('------不一样分割线-----')

#List 和字符串不一样的是，它的元素是可以改变的
list[0] = 9
list [2:5] = [13,14,15]
print(list)
list [1:] = [4,5,6]
print(list)
list [1:5] = [4,5,6] #语法没错 意思是 [1:5]设置成[4,5,6] out: [9, 4, 5, 6]
print(list)

#列表截取可以接收第三个参数，意思是步长，如果为负表示逆向读取例如：

def reverseWords(input):#用来实现逆向读取
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]# 第一个-1表示从最后一位开始，第三个-1表示逆
    output = ' '.join(inputwords)
    return output

if __name__ == "__main__":
    input = ' I like python'
    rw = reverseWords(input)
    print(rw) #python like I

#Tuple:可以索引可以截取不能修改，+进行拼接
#但可以包含可变对象如list，list可以修改

tup = (1,2,3,4,5,6)
print(tup[0])
tup1 = ()# 空元组
tup2 = (20,) #一个元素，需要在元素后面加都好
tup = ([20,2,2],)
tup[0][1]=20
print(tup) #20,20,2

#string list tuple 都属于 sequence 序列


#Set 集合:基本功能是进行成员关系测试和删除重复元素，用{}或者set()创建


sites = {'google','taobao','tencent'}
print(sites)

#成员测试
if 'google' in sites:
    print("google is in sites")
else :
    print("google is not in sites")

#set 可以进行集合运算

a = set('algebra')
b = set('geometry')

print(a) #不会按顺序输出{'r', 'b', 'l', 'g', 'a', 'e'}
print('a-b:',a - b) #差集
print('a | b',a | b) #并
print('a & b',a & b) #cross
print('a ^ b',a ^ b) # 异或

#Dictionary：用{}标识，
# 无序对象集合：
# 字典中的元素是通过键来存取而不是通过偏移存取——字典是一种映射类型

#key必须为不可变
dict = {}
dict['one'] = "analysis"
dict[2] = "linear algebra"
tinydict = {'course':'analysis','students':16,'teacher':'jz'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


del(dict)
#dict() 可以直接从键值对序列中构建字典
#函数名和变量名重名,用del
#如果前面已经由dict 了报错：'dict' object is not callable，不冲突是可以用的
td = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(td)
td = {x:x**2 for x in (2, 4, 6)} #加入循环，这是啥语法？字典推导式
print(td)
td = dict(Runoob=1, Google=2, Taobao=3) # 默认成字符串了？
print(td)









