
 var=input('15')
15
 age=('15')
 print(type(age))
<class 'str'>
 x=10
 print(type(x))
<class 'int'>
 y=10000000
 print(type(y))
<class 'int'>
 x=1.5
 print(type(x))
<class 'float'>
 
 x=-5
 print(type(x))
<class 'int'>
 
 print(type(500))
<class 'int'>
 print(type(500.5))
<class 'float'>
 print(type(true))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined
 print(type(3!=5))
<class 'bool'>
 print(type(true))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined
 print(type(true))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined
 x=true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
 print(type(true))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined
 print(type('true'))
<class 'str'>
 age=input("enter your age")
enter your age
>>> age="age"
>>> print(age+5)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(age+5)
TypeError: can only concatenate str (not "int") to str
>>> age=20
>>> print(age+5)
25
>>> age="age"
>>> print(int(age))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(int(age))
ValueError: invalid literal for int() with base 10: 'age'
>>> age="age"
>>> print(int(age)+5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(int(age)+5)
ValueError: invalid literal for int() with base 10: 'age'
>>> a=5
>>> b=5.5
>>> print(a+b)
10.5
>>> a=4.3
>>> print(a)
4.3
>>> a=2.3
>>> print(int(a))
2
>>> a=2.9
>>> print(int(a))
2
>>> print(round(8.9))
9
>>> print(int('age'))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(int('age'))
ValueError: invalid literal for int() with base 10: 'age'
>>> str(1)
'1'
>>> str(3.4)
'3.4'
>>> int('abc')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int('abc')
ValueError: invalid literal for int() with base 10: 'abc'
>>> str(3.5)
'3.5'
>>> float(1)
1.0
>>> int('5')
5
>>> x,y=8,5
>>> x+y
13
>>> a,b=10,20
>>> a,b=b+1,a+1
>>> a,b
(21, 11)
>>> 