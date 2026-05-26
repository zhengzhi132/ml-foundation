# 04｜函数

函数是一段**可重复使用**的代码块。写一次，到处调用。

---

## 一、定义与调用

用 `def` 定义函数，用 `()` 调用。

```python
def greet():
    print("你好！")

greet()          # 你好！
greet()          # 你好！（可以反复调用）
```

---

## 二、参数

### 位置参数

参数按**顺序**一一对应传入。

```python
def introduce(name, age):
    print(f"我叫 {name}，今年 {age} 岁")

introduce("小明", 18)   # 我叫 小明，今年 18 岁
introduce(18, "小明")   # 我叫 18，今年 小明 岁（顺序错乱，结果不对！）
```

### 默认参数

给参数赋予默认值，调用时可以不传。

```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}")

greet("小红")                 # 你好，小红
greet("小刚", "早上好")       # 早上好，小刚
greet("小丽", greeting="嗨")  # 嗨，小丽（推荐用关键字指定）
```

**注意**：默认参数必须写在位置参数**后面**。

```python
# 正确
def f(a, b=10): ...

# 错误
# def f(a=10, b): ...  ← 语法错误
```

### 关键字参数

调用时用 `参数名=值` 的方式，不依赖顺序。

```python
def show_info(name, age, city):
    print(f"{name} / {age} / {city}")

show_info(city="上海", name="小刚", age=20)  # 小刚 / 20 / 上海
```

---

## 三、返回值

用 `return` 把结果返回给调用方。

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# 不写 return → 返回 None
def nothing():
    pass

print(nothing())  # None
```

### 返回多个值（实际上是返回元组）

```python
def split_name(full_name):
    first = full_name[0]
    last = full_name[1:]
    return first, last  # 返回元组

x, y = split_name("张三")
print(x)  # 张
print(y)  # 三

# 等同于：
result = split_name("李四")
print(result)  # ('李', '四')
```

---

## 四、作用域

函数内部定义的变量**只在函数内有效**。

```python
x = 10  # 全局变量

def my_func():
    x = 5          # 局部变量（和全局的不是同一个）
    print("内部：", x)

my_func()          # 内部： 5
print("外部：", x) # 外部： 10
```

### 在函数内修改全局变量（不推荐）

```python
count = 0

def increment():
    global count   # 声明要修改全局变量
    count += 1

increment()
print(count)       # 1
```

**最佳实践**：尽量用返回值代替 `global`。

---

## 五、函数作为"小工具"

函数可以调用其他函数，组合使用。

```python
def double(n):
    return n * 2

def add_one(n):
    return n + 1

# 组合使用
x = 5
result = add_one(double(x))
print(result)  # 11（先翻倍 → 10，再加 1 → 11）
```

---

## 六、实用模式：提前返回

```python
def check_age(age):
    if age < 0:
        return "年龄不能为负数"
    if age < 18:
        return "未成年人"
    return "成年人"

print(check_age(-5))   # 年龄不能为负数
print(check_age(15))   # 未成年人
print(check_age(25))   # 成年人
```

---

## 七、完整的例子

```python
def create_student(name, scores=None):
    """创建一个学生信息字典"""
    if scores is None:
        scores = []
    
    avg = sum(scores) / len(scores) if scores else 0
    
    return {
        "name": name,
        "scores": scores,
        "average": avg
    }

s1 = create_student("小红", [85, 92, 78])
print(f"{s1['name']} 的平均分是 {s1['average']}")  
# 小红 的平均分是 85.0

s2 = create_student("小明")
print(f"{s2['name']} 的平均分是 {s2['average']}")  
# 小明 的平均分是 0
```

## 总结

- `def` 定义函数，`()` 调用函数
- **位置参数**：按顺序传参
- **默认参数**：有默认值，可省略
- **关键字参数**：用 `name=value` 传参，不依赖顺序
- **`return`**：返回值，不写则返回 `None`
- 函数内变量是**局部**的，不影响外部
- 可返回多个值（实际是元组）