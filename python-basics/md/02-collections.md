# 02｜列表、元组、字典、集合

四种常用容器，用来**存放多个数据**。

---

## 一、列表（list）

列表用 `[]` 创建，**可修改**，**有序**。

### 创建与索引

```python
fruits = ["苹果", "香蕉", "橘子"]
print(fruits[0])     # 苹果（索引从 0 开始）
print(fruits[-1])    # 橘子（-1 是最后一个）
print(fruits[1:3])   # ['香蕉', '橘子']（切片：左闭右开）
```

### 增删改

```python
# 增
fruits.append("葡萄")     # 末尾追加
fruits.insert(1, "草莓")  # 在索引 1 处插入
print(fruits)  # ['苹果', '草莓', '香蕉', '橘子', '葡萄']

# 删
fruits.remove("香蕉")     # 按值删除
popped = fruits.pop()     # 删除并返回末尾元素
del fruits[0]             # 按索引删除
print(fruits)  # ['草莓', '橘子']

# 改
fruits[0] = "蓝莓"
print(fruits)  # ['蓝莓', '橘子']
```

### 常用操作

```python
nums = [3, 1, 4, 1, 5, 9]
print(len(nums))       # 6（长度）
print(3 in nums)       # True（是否包含）
print(nums.count(1))   # 2（出现次数）
nums.sort()            # 排序
print(nums)            # [1, 1, 3, 4, 5, 9]
nums.reverse()         # 反转
print(nums)            # [9, 5, 4, 3, 1, 1]
```

---

## 二、元组（tuple）

元组用 `()` 创建，**不可修改**，**有序**。

```python
point = (3, 7)
print(point[0])     # 3
print(point[1])     # 7

# point[0] = 10    ← 报错！元组不能修改

# 解包（非常实用）
x, y = point
print(x, y)         # 3 7

# 单元素元组必须加逗号
single = (5,)       # 不加逗号就是 int 类型
print(type(single)) # <class 'tuple'>
```

**元组 vs 列表**：元组不可变，适合存放**不应修改**的数据（如坐标、配置等）。

---

## 三、字典（dict）

字典用 `{}` 创建，存的是 **键 → 值** 的映射。**键不可重复**。

### 创建与查改

```python
student = {
    "name": "小红",
    "age": 18,
    "city": "北京"
}

# 查
print(student["name"])    # 小红
print(student.get("age")) # 18（不存在返回 None，不报错）

# 改 / 增
student["age"] = 19       # 修改已有键
student["score"] = 95     # 新增键值对

# 删
del student["city"]       # 删除键值对
popped = student.pop("age")  # 删除并返回值
print(student)  # {'name': '小红', 'score': 95}
```

### 遍历字典

```python
info = {"name": "小刚", "age": 20}

for key in info:
    print(key, info[key])
# 输出：
# name 小刚
# age 20

for key, value in info.items():
    print(key, value)
# 同上
```

### 判断键是否存在

```python
d = {"a": 1, "b": 2}
print("a" in d)   # True
print("c" in d)   # False
```

---

## 四、集合（set）

集合用 `{}` 创建，**无序、不重复**。

```python
# 创建
s = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(s)  # {1, 2, 3, 4, 5, 6, 9}（自动去重，顺序不定）

# 增删
s.add(7)
s.remove(3)
print(s)  # {1, 2, 4, 5, 6, 7, 9}

# 集合运算（和数学上的集合一样）
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)  # {3, 4}（交集）
print(a | b)  # {1, 2, 3, 4, 5, 6}（并集）
print(a - b)  # {1, 2}（差集）
```

**注意**：空集合用 `set()`，不是 `{}`，因为 `{}` 是空字典。

---

## 五、快速参考

| 类型 | 可变 | 有序 | 重复 | 写法 |
|------|------|------|------|------|
| 列表 `list` | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| 元组 `tuple` | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| 字典 `dict` | ✅ | ❌（3.7+ 有序） | 键不重复 | `{"k": "v"}` |
| 集合 `set` | ✅ | ❌ | ❌ | `{1, 2, 3}` |

## 总结

- **列表**：最常用，存有序、可修改的数据
- **元组**：不可修改，适合存固定数据；可解包
- **字典**：通过键查找值，适合存有名字的字段
- **集合**：去重、交集/并集运算