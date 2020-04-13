#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#类定义
class Person:
    '''一个简单的类实例'''
    #定义基本属性
    personName=''
    age=0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    def __init__(self,personName,age):
        self.personName=personName
        self.age=age
        self.hobbies=[]

    def sayHi(self,content):
        print(f"{self.personName} 打印了{content}")
    def printAge(self):
        print(f"{self.personName},your age is {self.age}")
    def printHobbies(self):
        print(self.hobbies)
    def printSelfProperties(self):
        print(self)
        print(self.__class__)
    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.personName, self.age))


#实例化
oPerson=Person('sushee',36)

print(oPerson.personName)
oPerson.sayHi("我爱你，中国...")
oPerson.printAge()
oPerson.hobbies.append("basketball")
oPerson.hobbies.extend(["football","running","sing","swimming"])
oPerson.printHobbies()
oPerson.printSelfProperties()
oPerson.speak()

#类的继承，如果一种语言不支持继承，那么类就没什么意义
class Student(Person):
    grade=0
    def __init__(self,studentName,age,grade):
        # 调用父类的构造函数
        Person.__init__(self,studentName,age)
        self.grade=grade
    #覆盖父类的方法
    def speak(self):
        print(f"{self.personName}说：我{self.age}岁了，我在读{self.grade}年级，好好学习，天天向上")

oStudent=Student('小明',9,4)
oStudent.speak()
oStudent.sayHi("hello world!!!")

#Python 中类的多继承，需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
# python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
#另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))


# 多重继承
class sample(Speaker, Student):
    a = ''

    def __init__(self,name,age,grade,topic):
        Student.__init__(self, name,age,grade)
        Speaker.__init__(self, name,topic)


test = sample("小强",26,4,'Python')
test.speak()  # 方法名同，默认调用的是在括号中排前边父类的方法




