#--coding=utf-8--#

szName="hi %s, today is %d年%d月%d日!"% ('sushee',2020,3,1)
nAge=36
name2=f"hi sushee, My age is {nAge}"
print(name2)

multiLine='''hi
line1
line2 
<a href='http://www.baidu.com'>百度</a>'''
#将字符串的第一个字符转换为大写
szName=szName.capitalize()
print(szName)
print('hello'.center(50,'#'))
#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print('111hellho'.count('h',0,-1))
print('abc'.encode('utf-8'))
print(b'abc'.decode('utf-8'))
print('abc'.find('bc',0))
print("abcdefg".index('c'))
print("123#".isalnum())
print("abc".isalpha())
print("123a".isdigit())
print("abc#".islower())
print("ABc1".isupper())
print("123".isnumeric())
print(" ".isspace())
#用特定字符连接一个字符序列
print("a".join(('a','b','cd')))
#返回字符串长度
print(len("abc"))
#字符串左对齐
print("abc".ljust(5,'#'))
#字符串右对齐
print("abc".rjust(6,'0'))
#字符串转小写
print("abC".lower())
#字符串转大写
print("Abc".upper())
#截掉字符串左边的空格或指定字符
print(" cde ".lstrip())
#截掉字符串右边的空格或指定字符
print(" cde ".rstrip())
#截掉字符串左右2边的空格或指定字符
print(" cde ".strip())
print("#cde#".strip('#'))
'''maketrans 创建字符映射的转换表，两个字符串的长度必须相同，为一一对应的关系。
以下实例展示了使用maketrans() 方法将所有元音字母转换为指定的数字：
'''
intab = "aeiou"
outtab = "12345"
str = "this is string example....wow!!!"
trantab = str.maketrans(intab, outtab)
print (str.translate(trantab))
#返回字符串 str 中最大的字母。
print(max("abc","def"))
#返回字符串 str 中最小的字母。
print(min("abc"))
#字符串替换方法
print("abc".replace('a','d'))
#rfind 类似于find，只不过是从右边开始查找
print("abcdefg".rfind('f'))
#rindex 类似于index,不过是从右边开始查找
print("abcdefg".rindex('b'))
#num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
print("a b c d".split(" ",1))
'''Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。'''
print("a\nb\rb\rc".splitlines(True))
#startswith 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
print("abc".startswith('a'))
print("abc".endswith('c'))
#交换字符串大小写字母
print("AbC".swapcase())
#title(),返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print("hi baby i love you so much".title())
#translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

str = "this is string example....wow!!!"
print(str.translate(trantab))
#zfill 返回长度为 width 的字符串，原字符串右对齐，前面填充0
print("abc".zfill(50))
#isdecimal isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
print("is123".isdecimal())
print("123567".isdecimal())