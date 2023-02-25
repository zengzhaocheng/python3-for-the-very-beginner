# 
import re
print(re.match('www','www.runoob.com').span()) #起始位置!
print(re.match('com','www.runoob.com'))

print("------------------")

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1): ", matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))#group是正则表达式中被括号括起来的部分
else:
    print("No match!")

print('--------search-------')

print(re.search('www','www.runoob.com').span())
print(re.search('com','www.runoob.com').span())

print('-------search group--------')

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!")
    
print("-------search vs match---------")
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")


print('-------sub----------')
phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)


print('--------replace-------')
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('name'))
    return str(value * 2)
 
s = 'A23G4HFD567'
#第二个参数是repl
print(re.sub('(?P<name>\d+)', double, s))

print('--------compile----------')
pattern = re.compile(r'\d+') #至少有一个数字
m = pattern.match('one123345niohnfv')
print(m)
m = pattern.match('one123345niohnfv',3,10)
print(m)

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print( m ) 
print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
print(m.groups())


print("------findall-------")
result1 = re.findall(r'\d+','runoob 123 google 456')
 
pattern = re.compile(r'\d+')   # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
print(result3)


#多个匹配模式
result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)



print("----------finditer--------")
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )


print('---------split----------')
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('\w+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.') )  #???
print(re.split('\W+', ' runoob, runoob, runoob.', 1)  )  #???
print(re.split('a*', 'hello world'))#???