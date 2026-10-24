Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
type(a)
<class 'int'>
b = 12.3
type(b)
<class 'float'>
c = 2+5j
c
(2+5j)
type(c)
<class 'complex'>
s = "Codegnan"
type(s)
<class 'str'>
s
'Codegnan'
l=[1,2,3,4]
type(l)
<class 'list'>
k=[1,23.4,"56",[1,2,3]]
k
[1, 23.4, '56', [1, 2, 3]]
type(k)
<class 'list'>
l=[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
s='code'
id(s)
140737293412024
s+="gnan"
s
'codegnan'
s
'codegnan'
id(s)
1707701419312
l=[1,2,3]
id(l)
1707701542784
l.append(12)
l
[1, 2, 3, 12]
id(l)
1707701542784
l.pop()
12
l
[1, 2, 3]
id(l)
1707701542784
l
[1, 2, 3]
t=(1,2,3,4)
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,2.3)
t
(1, 2.3)
type(t)
<class 'tuple'>
s={34,1234,124321,1325,235,34,34,34,34,34}
s
{124321, 34, 1234, 235, 1325}
type(s)
<class 'set'>
d={1:"one",2:4,3:[1,2,3],5:(1,23)}
>>> d
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
>>> pro = {"pro_name":'laptop',"price":55000,"discount":10}
>>> pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
>>> type(d)
<class 'dict'>
>>> status =True
>>> type(status)
<class 'bool'>
>>> s = False
>>> type(s)
<class 'bool'>
>>> s=None
>>> type(s)
<class 'NoneType'>
