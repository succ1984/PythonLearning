#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#集合数据结构学习Demo  ,集合（set）是一个无序的不重复元素序列。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)       #集合去重功能
print("apple" in basket)
#集合运算
a=set('abcdef')
b=set('abc')
print(a-b)            #集合a中包含而集合b中不包含的元素
print(a|b)   #集合a或b中包含的所有元素
print(a&b)   #集中a或B中都包含的元素
print(a^b)   #不同时包含于a和b的元素
#添加操作
basket.add("peach")
print(basket)
basket.update({1,2})
print(basket)
basket.update([4,5])
print(basket)
basket.update((1,2,3))
print(basket)
#移除操作
basket.remove(1)
print(basket)
# basket.remove(1)   如果元素不存在，则会发生错误。
# print(basket)
basket.discard(2)     #如果元素不存在，不会发生错误
print(basket)
#pop() ,随机删除一个元素
popEle=basket.pop()
print(popEle)
print(basket)
#计算集合元素个数
print(len(basket))
#清空集合
basket1=basket.copy()
basket.clear()
print(basket)
print(basket1)
#判断元素是否在集合中
print("ape" in basket1)
#set.difference(set),返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
x={1,2,3}
y={2,5,8}
z=x.difference(y)
print(z)
#set.difference_update(set), difference_update() 方法用于移除两个集合中都存在的元素。
#difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合
# ，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
m={1,2,3}
n={2,3,4}
m.difference_update(n)
print(m)
#set.symmetric_difference(set) ,返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
c1={1,2,3}
c2={2,3,4}
c=c1.symmetric_difference(c2)
print(c)
#set.symmetric_difference_update(set), 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
set1={1,2,3}
set2={2,5,8}
set1.symmetric_difference_update(set2)
print(set1)
#union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
print({1,2,3}.union({4,5,6,3},{1,7}))
#intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
print({1,2,3}.intersection({1,2}))
print({1,2,3,4,5,6,7}.intersection({1,2,5},{1,2}))
#set.intersection_update(set1, set2 ... etc) 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
x={1,2,3}
y={1,2,3,4,5,6}
x.intersection_update(y)
print(x)
#isdisjoint, set.isdisjoint(set)，判断2个集中是否包含相同的元素，如果没有返回True,否则返回False
print({1,2}.isdisjoint({6,3}))
#issubset(),set.issubset(set) 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
print({1,2}.issubset({1}))
#issuperset, 用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
print({1,2,3}.issuperset({1}))











