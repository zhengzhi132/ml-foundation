import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()
text = text.replace("，", "")  # 去掉逗号
text = text.replace("。", "")  # 去掉句号
text = text.replace("！", "")  # 去掉感叹号
text = text.lower()  # 转小写

words = text.split()
counter = {}
for word in words:
    counter[word] = counter.get(word, 0 ) + 1
sorted_counter = sorted(counter.items(), key = lambda x: x[1], reverse = True)
for word, count in sorted_counter:
    print(f"{word}: {count}")