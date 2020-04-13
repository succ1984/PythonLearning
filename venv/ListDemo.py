#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 列表方法学习
list1 = ['Google', 'Runoob', 1997, 2000];
list2=[1,2,3,4,5,6,7]
print("List1[2]:",list1[2])
print("list2[1:5]",list2[1:5])
#修改列表项的值
list1[3]=2020
print("list1[3]:",list1[3])
print(list1)
#可以使用 del 语句来删除列表的的元素
del list1[2]
print("list1[2]:",list1[2])
print(list1)
#列表长度
print(len(list1))
#列表组合
print([1,2,3]+[4,5,6,'abc'])
#列表重复
print(['hi!']*4)
#查看元素是否存在于列表中
print(1 in[1,2,3])
#列表元素迭代
for x in [1,2,3,'a','b','c']:
    print(x)
#列表截取
print(list2[1])
print(list2[1:3])
print(list2[-1])
list3=list1+list2
print(list3)
list3+=list1
print(list3)
#列表嵌套
list4=[list3,'sushee']
print(list4)
print(list4[0])
print(list4[1])
#列表函数
#列表长度
print(len(list4))
#最大值
print(max(list4[1]))
#最小值
list5=[1,2,3]
print(min(list5))
#将元组转换为列表list(tuple)
tuplePeople=('su','c','c')
list6=list(tuplePeople)
print(list6)
#list 方法
#append() 方法用于在列表末尾添加新的对象。
list6.append('你好啊')
print(list6)
#count() 方法用于统计某个元素在列表中出现的次数
print(list6.count('c'))
#list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）,
# seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
list6.extend(['i','love','you'])
print(list6)
list6.extend(tuplePeople)
print(list6)
setPeople={',','你','也','是','啊'}
list6.extend(setPeople)
print(list6)
#index
print(list6.index('c'))
#	list.insert(index, obj),insert() 函数用于将指定对象插入列表的指定位置。
list6.insert(1,'haha!!!')
print(list6)
#list.pop([index=-1]),移除列表中的一个元素， 默认为最后一个元素，即index=-1,index不能超过列表的最大长度
popValue=list6.pop()
print(list6)
print(popValue)
#  list.remove(obj),remove() 函数用于移除列表中某个值的第一个匹配项。 该方法没有返回值但是会移除列表中的某个值的第一个匹配项。
list6.remove('su')
print(list6)
#list.reverse() ,reverse() 函数用于反向列表中元素。
list6.reverse()
print(list6)
# list.sort( key=None, reverse=False) ,sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
list6.sort()
print(list6)
list6.reverse()
print(list6)
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
def takeSecond(elem):
    return elem[1]
random.sort(key=takeSecond)
print(random)
#清空列表
list6.clear()
print(list6)
#复制列表
listCopy=list2.copy()
print(listCopy)

#











    
