---
layout: post
title: " Python 字符串作为函数名调用 "
tagline: " Python  "
categories: Python
author: "Hu Tianyun"
meta: "Springfield"
---
## 参考
[[str->fun-name]](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string)

[[python-func-globals]](http://www.runoob.com/python/python-func-globals.html)

[[python-func-getattr]](http://www.runoob.com/python/python-func-getattr.html)
## 用法
```python
class A:
    def __init__(self):
        pass

    def sampleFunc(self, arg):
        print('you called sampleFunc({})'.format(arg))

m = globals()['A']()
func = getattr(m, 'sampleFunc')
func('sample arg')

# Sample, all on one line
getattr(globals()['A'](), 'sampleFunc')('sample arg')
```

### 解释

####Python globals() 函数
globals() 函数会以字典类型返回当前位置的全部全局变量。
##### 实例
```python
>>>a='runoob'
>>> print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 'runoob', '__package__': None}
```

#### Python getattr() 函数
getattr() 函数用于返回一个对象属性值。
##### 实例
```python
>>>class A(object):
...     bar = 1
... 
>>> a = A()
>>> getattr(a, 'bar')        # 获取属性 bar 值
1
>>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
3
```