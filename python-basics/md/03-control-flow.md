# 03｜条件语句与循环

控制代码的执行流程：**什么条件下做什么事**、**重复做什么事**。

---

## 一、条件语句：if / elif / else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "不及格"

print(grade)  # B
```

**规则：**
- `if` 后面的条件为 `True` 时执行该分支
- `elif` 是 "else if" 的简写，可以有多个
- `else` 是兜底，可省略
- 用**缩进**（4 个空格）表示代码块

### 布尔值判断技巧

```python
# 以下值在 if 中被视为 False
if None:   print("不会执行")
if 0:      print("不会执行")
if "":     print("不会执行")
if []:     print("不会执行")
if {}:     print("不会执行")

# 其余所有值都是 True
if "hello": print("会执行")  # ✓
if [1, 2]:  print("会执行")  # ✓
```

### 常用写法：三元表达式

```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)  # 成年

# 等同于：
if age >= 18:
    status = "成年"
else:
    status = "未成年"
```

---

## 二、for 循环

`for` 用来**遍历**一个可迭代对象（列表、字符串、字典等）。

### 遍历列表

```python
names = ["张三", "李四", "王五"]

for name in names:
    print(name)
# 输出：
# 张三
# 李四
# 王五
```

### 遍历字符串

```python
for ch in "Python":
    print(ch)
# P
# y
# t
# h
# o
# n
```

### 遍历字典

```python
student = {"name": "小红", "age": 18, "city": "北京"}

for key in student:
    print(key, student[key])

# 更优雅的方式：
for key, value in student.items():
    print(key, value)
```

### range() — 生成数字序列

```python
# range(5) → 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

print()

# range(2, 6) → 2, 3, 4, 5
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5

print()

# range(0, 10, 2) → 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
```

### enumerate() — 同时拿到索引和值

```python
fruits = ["苹果", "香蕉", "橘子"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 输出：
# 0: 苹果
# 1: 香蕉
# 2: 橘子
```

---

## 三、while 循环

`while` 在条件为 `True` 时一直重复执行。

```python
# 从 5 数到 1
count = 5
while count > 0:
    print(count)
    count -= 1
print("发射！")
# 5
# 4
# 3
# 2
# 1
# 发射！
```

### 无限循环 → 用 break 退出

```python
while True:
    cmd = input("输入 exit 退出：")
    if cmd == "exit":
        break
    print("你输入了：", cmd)
```

---

## 四、break 与 continue

- `break`：**跳出**整个循环
- `continue`：**跳过**本次循环，进入下一次

```python
for i in range(10):
    if i == 3:
        continue   # 跳过 3
    if i == 7:
        break      # 到 7 结束
    print(i, end=" ")
# 0 1 2 4 5 6
```

---

## 五、综合示例

```python
# 找出列表中的偶数
numbers = [12, 7, 9, 18, 3, 22, 5]
even_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers)  # [12, 18, 22]
```

```python
# 用 enumerate + 条件判断来「带索引地筛选」
names = ["张三", "李四", "王五", "赵六"]
for i, name in enumerate(names):
    if name == "王五":
        print(f"找到了！索引是 {i}")  # 找到了！索引是 2
```

## 总结

- **if / elif / else**：条件判断，注意缩进
- **for 循环**：遍历列表、字符串、字典等
- **range()**：生成整数序列，配合 for 遍历
- **enumerate()**：遍历时同时获取索引
- **while 循环**：条件为真时重复，注意别写成死循环
- **break**：跳出循环 / **continue**：跳过本次