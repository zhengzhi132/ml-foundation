# 06｜字符串处理

字符串是 Python 中最常用的数据类型之一。这里只讲四个最实用的操作：`split`、`join`、`replace`、f-string。

---

## 一、split() — 分割字符串

将字符串按指定分隔符**切分成列表**。

```python
text = "苹果,香蕉,橘子,葡萄"
fruits = text.split(",")
print(fruits)  # ['苹果', '香蕉', '橘子', '葡萄']
```

### 按空格分割（默认行为）

```python
sentence = "Hello World Python"
words = sentence.split()
print(words)  # ['Hello', 'World', 'Python']
```

### 限制分割次数

```python
data = "a-b-c-d"
print(data.split("-", 2))   # ['a', 'b', 'c-d']（只切前 2 个 -）
print(data.split("-", 1))   # ['a', 'b-c-d']（只切第 1 个 -）
```

### 实际应用：解析 CSV 风格数据

```python
line = "张三,18,北京"
parts = line.split(",")
name, age, city = parts
print(f"{name} / {age} / {city}")  # 张三 / 18 / 北京
```

---

## 二、join() — 合并字符串

与 `split` 相反：将列表中的字符串**拼接成一个**。

```python
fruits = ["苹果", "香蕉", "橘子"]
result = "、".join(fruits)
print(result)  # 苹果、香蕉、橘子
```

**重点**：分隔符写在**前面**，列表写在 `join()` 的参数里。

```python
words = ["Hello", "World", "Python"]
print(" ".join(words))    # Hello World Python
print(" -> ".join(words)) # Hello -> World -> Python
print("".join(words))     # HelloWorldPython（无分隔符）
```

### 常见用途：拼接路径

```python
parts = ["data", "2024", "report.txt"]
path = "/".join(parts)
print(path)  # data/2024/report.txt
```

---

## 三、replace() — 替换文本

将字符串中的**某段子串替换成另一段**。

```python
text = "我喜欢吃苹果"
new_text = text.replace("苹果", "香蕉")
print(new_text)  # 我喜欢吃香蕉
```

### 限制替换次数

```python
text = "one one one one"
print(text.replace("one", "1"))          # 1 1 1 1（全部替换）
print(text.replace("one", "1", 2))        # 1 1 one one（只替换前 2 次）
```

### 实际应用：清洗数据

```python
# 去掉文本中的标点符号
text = "Hello, World! How are you?"
cleaned = text.replace(",", "").replace("!", "").replace("?", "")
print(cleaned)  # Hello World How are you
```

```python
# 标准化空格
text = "这是   一段   有   很多   空格的  文字"
normalized = text.replace("  ", " ")  # 两个空格 → 一个空格
print(normalized)  # 这是 一段 有 很多 空格的 文字
```

---

## 四、f-string — 格式化字符串（Python 3.6+）

在字符串前加 `f`，用 `{变量名}` 在字符串中插入值。

```python
name = "小红"
age = 18
print(f"我叫 {name}，今年 {age} 岁")  
# 我叫 小红，今年 18 岁
```

### 在 f-string 中调用方法

```python
name = "alice"
print(f"大写：{name.upper()}")   # 大写：ALICE
print(f"首字母大写：{name.title()}")  # 首字母大写：Alice
```

### 在 f-string 中写表达式

```python
a, b = 10, 3
print(f"{a} + {b} = {a + b}")   # 10 + 3 = 13
print(f"{a} / {b} = {a / b:.2f}")  # 10 / 3 = 3.33（保留两位小数）
```

### 对齐与填充

```python
name = "小明"
print(f"|{name:>10}|")   # |       小明|（右对齐，宽度 10）
print(f"|{name:<10}|")   # |小明       |（左对齐）
print(f"|{name:^10}|")   # |   小明    |（居中对齐）
```

---

## 五、其他常用字符串方法

```python
text = "  Hello, Python!  "

print(text.strip())        # "Hello, Python!"（去掉首尾空格）
print(text.upper())        # "  HELLO, PYTHON!  "（转大写）
print(text.lower())        # "  hello, python!  "（转小写）
print(text.startswith(" "))  # True（是否以空格开头）
print(text.endswith("!"))    # True（是否以 ! 结尾）
print(len(text))             # 18（字符串长度）
```

### 字符串是不可变的

```python
s = "Hello"
# s[0] = "h"  ← 报错！字符串不能修改

# 正确做法：生成新字符串
s = "h" + s[1:]
print(s)  # hello
```

---

## 六、综合示例

### 示例 1：统计单词数量

```python
text = "Python is great and Python is fun"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'Python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
```

### 示例 2：清理并格式化输出

```python
raw_data = "  张三,18  ,  北京  "
parts = raw_data.split(",")
cleaned = [p.strip() for p in parts]  # 去掉每个字段的空格
print(cleaned)  # ['张三', '18', '北京']

# 格式化输出
print(f"姓名：{cleaned[0]} | 年龄：{cleaned[1]} | 城市：{cleaned[2]}")
# 姓名：张三 | 年龄：18 | 城市：北京
```

### 示例 3：拼接路径

```python
def build_path(folder, filename):
    return "/".join([folder, filename])

print(build_path("docs", "readme.txt"))  # docs/readme.txt
print(build_path("data/2024", "report.csv"))  # data/2024/report.csv
```

## 总结

- **`split()`**：字符串 → 列表（按分隔符切分）
- **`join()`**：列表 → 字符串（用分隔符拼接）
- **`replace()`**：替换子串，可限制替换次数
- **f-string**：`f"内容 {变量}"`，最推荐的格式化方式
- 字符串**不可变**，所有操作都返回新字符串