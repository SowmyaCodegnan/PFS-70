Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b = 10.3
int(b)
10
complex(b)
(10.3+0j)
str(b)
'10.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
bool(0.0)
False
c = 3+4j
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(3+4j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
s
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
bool(0+0j)
False
s = 'codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
a='1019'
int(a)
1019
float(a)
1019.0
complex(a)
(1019+0j)
list(a)
['1', '0', '1', '9']
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'e', 'o', 'c', 'd', 'a', 'g', 'n'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
bool('')
False
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4)
int(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
'(1, 2, 3, 4)'
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
dict(t)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
int(s)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
[1, 2, 3, 4, 5]
tuple(s)
(1, 2, 3, 4, 5)
str(d)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    str(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
str(s)
'{1, 2, 3, 4, 5}'
dict(s)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d={1:1,2:2,3:3,4:4}
int(d)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(d)
'{1: 1, 2: 2, 3: 3, 4: 4}'
list(d)
[1, 2, 3, 4]
tuple(d)
(1, 2, 3, 4)
set(d)
{1, 2, 3, 4}
bool(d)
True
a = True
int(a)
1
float(a)
1.0
complex(a)
(1+0j)
str(a)
'True'
list(a)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> '''
... int -> float,complex,s,b
... fl->in,com,s,b
... com->s,b
... s->i,f,c,l,t,s,b
... l->s,t,s,b
... t->s,l,s,b
... s->s,l,t,b
... d->s,l,t,s,b
... b->i,f,c,s
... '''
'\nint -> float,complex,s,b\nfl->in,com,s,b\ncom->s,b\ns->i,f,c,l,t,s,b\nl->s,t,s,b\nt->s,l,s,b\ns->s,l,t,b\nd->s,l,t,s,b\nb->i,f,c,s\n'
