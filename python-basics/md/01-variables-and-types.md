# 01｜变量与数据类型

Python 的变量**不需要提前声明类型**，直接赋值即可。Python 会自动推断值的类型。

## 1. 变量赋值

```python
# 用 = 给变量赋值
name = "小明"
age = 25
height = 1.75
is_student = True

print(name)        # 小明
print(age)         # 25
print(height)      # 1.75
print(is_student)  # True
```

**要点：**
- 等号右边先计算，结果赋给左边变量
- 变量名区分大小写：`Name` 和 `name` 是两个不同的变量
- 变量名不能以数字开头，不能包含空格，不能是 `if`、`for` 这类关键字

## 2. 基本数据类型

| 类型 | 英文名 | 示例 | 说明 |
|------|--------|------|------|
| 整数 | `int` | `42`, `-3`, `0` | 不带小数点的数 |
| 浮点数 | `float` | `3.14`, `-0.5`, `1.0` | 带小数点的数 |
| 字符串 | `str` | `"你好"`, `'Python'` | 用引号包裹的文本 |
| 布尔值 | `bool` | `True`, `False` | 只有两个值 |

```python
# 查看变量的类型
a = 100
print(type(a))       # <class 'int'>

b = 3.14
print(type(b))       # <class 'float'>

c = "Hello"
print(type(c))       # <class 'str'>

d = True
print(type(d))       # <class 'bool'>
```

## 3. 类型转换

```python
# 字符串 → 数字
s = "123"
n = int(s)
print(n + 1)         # 124

# 数字 → 字符串
age = 18
msg = "我今年 " + str(age) + " 岁"
print(msg)           # 我今年 18 岁

# 数字 → 布尔
print(bool(0))       # False
print(bool(1))       # True
print(bool(-5))      # True（非零即真）
```

## 4. 常见陷阱

```python
# int 和 str 不能直接拼接
# print("年龄是" + 18)   ← 报错！TypeError

# 正确做法：先将 int 转成 str
print("年龄是" + str(18))  # 年龄是 18

# 浮点数精度问题（了解即可）
print(0.1 + 0.2)      # 0.30000000000000004（不是精确的 0.3）
```

## 5. type() 与 isinstance()

```python
# type() —— 获取类型
x = 3.14
print(type(x) == float)         # True

# isinstance() —— 判断是否属于某类型（推荐）
print(isinstance(x, float))     # True
print(isinstance(x, (int, float)))  # True（是 int 或 float）
```

## 总结

- Python 变量**动态类型**：不需要写类型，类型由赋的值决定
- 四大基础类型：`int`、`float`、`str`、`bool`
- 类型之间可以转换：`int()`、`str()`、`float()`、`bool()`
- 用 `type()` 或 `isinstance()` 检查类型