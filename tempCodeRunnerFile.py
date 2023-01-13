td = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(td)
td = {x:x**2 for x in (2, 4, 6)} #加入循环，这是啥语法？字典推导式
print(td)
td = dict(Runoob=1, Google=2, Taobao=3) # 默认成字符串了？
print(td)
