print('hello')
drinks=['可乐','脉动','芬达','qixi']
print(drinks)
#访问列表内的某个元素
drinks[2]
print(drinks[2].title())
#访问某些元素[切片]
print(drinks[0:2])
#在列表末尾添加元素
# 第二次提交代码修改
drinks.append('雪花啤酒')
print(drinks)
#在任意位置添加元素
drinks.insert(1,'奶茶')
print(drinks)
#删除:#删除列表内的某个元素
del drinks[2]
print(drinks)
#pop()删除元素：
#()删除最后一个元素 
drinks.pop()
print(drinks)
#(1)删除指定位置元素
drinks.pop(1)
print(drinks)


for i in range(1,11):
  print(i)
#list生成列表
num=list(range(1,11))
print(num)
#生成1-1 

# 第二次提交代码新增

