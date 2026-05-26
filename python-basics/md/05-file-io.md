# 05｜文件读写

Python 用内置的 `open()` 函数打开文件，配合 `read()` / `write()` 来读写内容。

**核心原则**：用完要关闭文件 —— 但用 `with` 语句会自动处理。

---

## 一、写文件

### 基本写法

```python
file = open("test.txt", "w", encoding="utf-8")
file.write("Hello, World!\n")
file.write("第二行内容\n")
file.close()  # 记得关闭！
```

每次 `open` 搭配 `close` 容易忘记，所以更推荐下面的 `with` 写法。

### 推荐写法：with 语句

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("第二行内容\n")
# 缩进结束后，文件自动关闭
```

**`open()` 的模式参数：**

| 模式 | 含义 | 说明 |
|------|------|------|
| `"w"` | write | 写入，**覆盖**已有内容 |
| `"a"` | append | 追加，在原内容后面继续写 |
| `"r"` | read | 读取（默认模式） |

### 写多行

```python
lines = ["第一行", "第二行", "第三行"]

with open("test.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
```

---

## 二、读文件

### 读取全部内容

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
# 第一行
# 第二行
# 第三行
```

### 按行读取

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        # 每行末尾有换行符 \n，用 strip() 去掉
        print(line.strip())
```

### 读取到列表

```python
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)  # ['第一行\n', '第二行\n', '第三行\n']

# 去掉换行符
lines = [line.strip() for line in lines]
print(lines)  # ['第一行', '第二行', '第三行']
```

---

## 三、追加内容

```python
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的一行\n")
```

`"a"` 模式不会清空原有内容，新内容写在末尾。

---

## 四、检查文件是否存在

```python
import os

if os.path.exists("test.txt"):
    print("文件存在")
else:
    print("文件不存在")
```

---

## 五、实际案例

### 案例 1：记录日志

```python
def log_message(msg):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[LOG] {msg}\n")

log_message("程序启动")
log_message("用户登录成功")
log_message("处理完成")
```

### 案例 2：读取配置

```python
# 假设 config.txt 内容为：
# name=小红
# age=18
# city=北京

config = {}
with open("config.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            config[key] = value

print(config)
# {'name': '小红', 'age': '18', 'city': '北京'}
```

### 案例 3：复制文件

```python
def copy_file(src, dst):
    """将 src 文件内容复制到 dst 文件"""
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)

copy_file("test.txt", "backup.txt")
```

---

## 六、编码问题

始终指定 `encoding="utf-8"`，否则 Windows 上可能出现乱码。

```python
# 正确
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("中文内容")
```

## 总结

- **写文件**：`open("文件", "w", encoding="utf-8")`
- **读文件**：`open("文件", "r", encoding="utf-8")`
- **追加**：`open("文件", "a", encoding="utf-8")`
- **永远用 `with` 语句**，不需要手动 `close()`
- **`"w"` 会覆盖**，**`"a"` 会追加**
- 按行读取时，用 `strip()` 去掉换行符
- 涉及中文时**务必指定 `encoding="utf-8"`**