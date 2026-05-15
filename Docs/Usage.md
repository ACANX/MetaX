## 使用指南


---

### 📦 安装

#### 首次安装

使用pip安装MetaX库：

```bash
pip install metax
```

#### 升级到最新版本

升级已安装的MetaX到最新版本：

```bash
pip install metax --upgrade
```

#### 从TestPyPI安装（测试版本）

如果你想测试尚未发布到正式PyPI的版本：

```bash
pip install --index-url https://test.pypi.org/simple/ metax
```

#### 验证安装

安装完成后，验证是否安装成功：

```bash
python3 -c "import metax; print('MetaX版本:', metax.__version__)"
```

输出示例：
```
MetaX版本: 0.1.2
```

---

### 🚀 快速开始

#### 基础示例

```python
import metax

# 问候函数
print(metax.hello("世界"))  # 输出: 你好, 世界!
print(metax.hello("PyPI"))  # 输出: 你好, PyPI!
```

---

### 📚 功能模块

MetaX提供以下功能模块：

#### 1. 数学运算（base/math）

##### 基础运算

```python
import metax

# 四则运算
print(metax.add(10, 5))        # 加法: 15
print(metax.subtract(10, 5))   # 减法: 5
print(metax.multiply(10, 5))   # 乘法: 50
print(metax.divide(10, 5))     # 除法: 2.0

# 除法异常处理
try:
    metax.divide(10, 0)
except ZeroDivisionError as e:
    print(f"错误: {e}")  # 输出: 错误: 除数不能为0
```

##### 高级运算

```python
import metax

# 幂运算和开方
print(metax.power(2, 3))       # 幂运算: 8.0
print(metax.sqrt(16))          # 平方根: 4.0
print(metax.cbrt(27))          # 立方根: 3.0

# 三角函数（参数为弧度）
import math
print(metax.sin(math.pi / 2))  # 正弦: 1.0
print(metax.cos(0))            # 余弦: 1.0
print(metax.tan(math.pi / 4))  # 正切: 1.0

# 对数函数
print(metax.log(math.e))       # 自然对数: 1.0
print(metax.log10(100))        # 常用对数: 2.0
print(metax.log2(8))           # 二进制对数: 3.0

# 取整函数
print(metax.abs(-5))           # 绝对值: 5.0
print(metax.round(3.7))        # 四舍五入: 4.0
print(metax.floor(3.7))        # 向下取整: 3
print(metax.ceil(3.2))         # 向上取整: 4

# 数论函数
print(metax.factorial(5))      # 阶乘: 120
print(metax.gcd(12, 8))        # 最大公约数: 4
print(metax.lcm(12, 8))        # 最小公倍数: 24
```

#### 2. 字符串处理（util/string）

##### 格式化工具

```python
import metax

# 大小写转换
print(metax.capitalize("hello"))      # 首字母大写: Hello
print(metax.title("hello world"))     # 每个单词首字母大写: Hello World
print(metax.upper("hello"))           # 转大写: HELLO
print(metax.lower("HELLO"))           # 转小写: hello
print(metax.swapcase("Hello"))        # 大小写互换: hELLO

# 字符串操作
print(metax.reverse("hello"))         # 反转: olleh
print(metax.truncate("Hello World", 8))  # 截断: Hello...

# 去除空白
print(metax.strip("  hello  "))       # 去除首尾空白: hello
print(metax.lstrip("  hello  "))      # 去除左侧空白: hello  
print(metax.rstrip("  hello  "))      # 去除右侧空白:   hello

# 命名转换
print(metax.camel_to_snake("helloWorld"))  # 驼峰转下划线: hello_world
print(metax.snake_to_camel("hello_world")) # 下划线转驼峰: helloWorld

# 脱敏处理
print(metax.mask("13812345678", 3, 4))  # 手机号脱敏: 138****5678
print(metax.mask("张三李四王五", 1, 1))  # 姓名脱敏: 张***五

# 格式化工具
print(metax.format_size(1024000))      # 文件大小: 1000.00 KB
print(metax.format_number(1234567.89)) # 数字格式化: 1,234,567.89
```

##### 验证工具

```python
import metax

# 类型判断
print(metax.is_empty(""))              # 判断空字符串: True
print(metax.is_numeric("123.45"))      # 判断数字: True
print(metax.is_integer("123"))         # 判断整数: True
print(metax.is_alpha("hello"))         # 判断字母: True
print(metax.is_alphanumeric("hello123")) # 判断字母数字: True

# 联系方式验证
print(metax.is_email("test@example.com"))    # 邮箱验证: True
print(metax.is_phone_cn("13812345678"))      # 手机号验证: True
print(metax.is_id_card_cn("110101199001011234")) # 身份证验证: True

# 网络相关验证
print(metax.is_url("https://www.example.com"))  # URL验证: True
print(metax.is_ip("192.168.1.1"))               # IP验证: True

# 其他验证
print(metax.is_hex_color("#FF5733"))     # 十六进制颜色: True
print(metax.is_date("2024-01-15"))       # 日期验证: True
print(metax.is_chinese("你好"))          # 中文验证: True
print(metax.contains_chinese("hello你好")) # 包含中文: True

# 长度验证
print(metax.length_between("hello", 1, 10))  # 长度范围: True

# 正则匹配
print(metax.matches("hello123", r"hello\d+"))  # 正则匹配: True
```

#### 3. 日期时间工具（util/datetime）

```python
import metax
from datetime import datetime, date

# 获取当前时间
print(metax.now())              # 当前时间: 2024-01-15 10:30:45
print(metax.today())            # 今天日期: 2024-01-15
print(metax.timestamp())        # 时间戳（秒）: 1705285845
print(metax.timestamp_ms())     # 时间戳（毫秒）: 1705285845123

# 时间戳转换
ts = metax.timestamp()
print(metax.from_timestamp(ts))  # 时间戳转字符串: 2024-01-15 10:30:45

# 解析和格式化
dt = metax.parse("2024-01-15 10:30:00")
print(metax.format(dt, "%Y年%m月%d日"))  # 自定义格式: 2024年01月15日

# 时间计算
dt = datetime.now()
print(metax.add_days(dt, 7))     # 加7天
print(metax.add_hours(dt, 2))    # 加2小时
print(metax.add_minutes(dt, 30)) # 加30分钟

# 时间差计算
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 15)
print(metax.diff_days(start, end))    # 天数差: 14
print(metax.diff_seconds(start, end)) # 秒数差: 1209600

# 日期判断
dt = date(2024, 1, 15)
print(metax.is_weekend(dt))      # 是否周末: False
print(metax.is_weekday(dt))      # 是否工作日: True

# 其他工具
birth_date = date(1990, 5, 20)
print(metax.get_age(birth_date))      # 计算年龄: 33
print(metax.get_quarter(dt))          # 获取季度: 1
print(metax.get_week_of_year(dt))     # 年中第几周: 3
print(metax.get_day_of_year(dt))      # 年中第几天: 15
```

#### 4. 文件操作工具（util/file）

```python
import metax

# 文本文件操作
metax.write_text("test.txt", "Hello, MetaX!")
content = metax.read_text("test.txt")
print(content)  # 输出: Hello, MetaX!

# 按行读写
lines = ["第一行", "第二行", "第三行"]
metax.write_lines("lines.txt", lines)
read_lines = metax.read_lines("lines.txt")

# JSON文件操作
data = {"name": "MetaX", "version": "0.1.2"}
metax.write_json("config.json", data)
loaded_data = metax.read_json("config.json")

# 文件信息
print(metax.exists("test.txt"))        # 文件是否存在: True
print(metax.is_file("test.txt"))       # 是否为文件: True
print(metax.is_dir("D:/Projects"))     # 是否为目录: True
print(metax.get_size("test.txt"))      # 文件大小（字节）
print(metax.get_extension("test.txt")) # 扩展名: .txt
print(metax.get_filename("D:/test.txt")) # 文件名: test.txt
print(metax.get_basename("D:/test.txt")) # 文件名（无扩展名）: test
print(metax.get_parent("D:/test.txt"))   # 父目录: D:/

# 路径操作
path = metax.join_path("D:", "Projects", "MetaX", "test.txt")
print(path)  # 输出: D:Projects\MetaX\test.txt

# 目录操作
metax.create_dir("D:/test/new_dir")    # 创建目录（支持多级）

# 文件操作
metax.copy_file("source.txt", "dest.txt")  # 复制文件
metax.move("old_path.txt", "new_path.txt") # 移动文件
metax.rename("old_name.txt", "new_name.txt") # 重命名

# 列出文件
files = metax.list_files("D:/Projects", "*.py")  # 列出所有.py文件
dirs = metax.list_dirs("D:/Projects")             # 列出所有子目录

# 文件哈希
md5 = metax.get_md5("test.txt")        # 计算MD5
sha256 = metax.get_sha256("test.txt")  # 计算SHA256

# 删除操作（谨慎使用）
# metax.delete_file("test.txt")        # 删除文件
# metax.delete_dir("D:/test", force=True)  # 删除目录（force=True强制删除非空目录）
```

---

### 💡 实用示例

#### 示例1：批量处理手机号脱敏

```python
import metax

phone_numbers = [
    "13812345678",
    "15987654321",
    "18611112222"
]

for phone in phone_numbers:
    masked = metax.mask(phone, 3, 4)
    print(f"原始: {phone} -> 脱敏: {masked}")

# 输出:
# 原始: 13812345678 -> 脱敏: 138****5678
# 原始: 15987654321 -> 脱敏: 159****4321
# 原始: 18611112222 -> 脱敏: 186****2222
```

#### 示例2：计算文件大小统计

```python
import metax

file_sizes = [1024, 2048, 5120, 10240, 204800]

total_size = 0
for size in file_sizes:
    total_size += size
    print(f"文件大小: {metax.format_size(size)}")

print(f"\n总大小: {metax.format_size(total_size)}")

# 输出:
# 文件大小: 1.00 KB
# 文件大小: 2.00 KB
# 文件大小: 5.00 KB
# 文件大小: 10.00 KB
# 文件大小: 200.00 KB
#
# 总大小: 218.00 KB
```

#### 示例3：验证用户输入

```python
import metax

def validate_user_input(email, phone, age_str):
    """验证用户输入"""
    errors = []
    
    # 验证邮箱
    if not metax.is_email(email):
        errors.append("邮箱格式不正确")
    
    # 验证手机号
    if not metax.is_phone_cn(phone):
        errors.append("手机号格式不正确")
    
    # 验证年龄
    if not metax.is_integer(age_str):
        errors.append("年龄必须是整数")
    elif not metax.length_between(age_str, 1, 3):
        errors.append("年龄长度不正确")
    
    return errors if errors else None

# 测试
errors = validate_user_input("test@example.com", "13812345678", "25")
if errors:
    print("验证失败:", errors)
else:
    print("验证通过！")
```

#### 示例4：日期计算工具

```python
import metax
from datetime import datetime

def calculate_deadline(start_date, work_days):
    """计算工作日后的截止日期"""
    current = start_date
    added_days = 0
    
    while added_days < work_days:
        current = metax.add_days(current, 1)
        if metax.is_weekday(current):
            added_days += 1
    
    return current

# 计算10个工作日后的日期
start = datetime.now()
deadline = calculate_deadline(start, 10)
print(f"开始日期: {metax.format(start)}")
print(f"截止日期: {metax.format(deadline)}")
```

---

### 🎯 最佳实践

#### 1. 导入建议

```python
# 推荐：导入整个包
import metax
result = metax.add(1, 2)

# 或者：导入特定模块
from metax.base.math import basic
result = basic.add(1, 2)

# 或者：导入特定函数
from metax import add, subtract
result = add(1, 2)
```

#### 2. 错误处理

```python
import metax

# 除法异常处理
try:
    result = metax.divide(10, 0)
except ZeroDivisionError as e:
    print(f"错误: {e}")

# 平方根异常处理
try:
    result = metax.sqrt(-1)
except ValueError as e:
    print(f"错误: {e}")
```

#### 3. 类型提示

MetaX的所有函数都提供了类型提示，IDE会自动提示参数类型和返回类型：

```python
import metax

# IDE会自动提示：
# add(a: float, b: float) -> float
result: float = metax.add(1.5, 2.5)
```

---

### 📖 完整API列表

#### 数学运算
- **基础运算**: `add`, `subtract`, `multiply`, `divide`
- **高级运算**: `power`, `sqrt`, `cbrt`, `sin`, `cos`, `tan`, `log`, `log10`, `log2`
- **取整函数**: `abs`, `round`, `floor`, `ceil`
- **数论函数**: `factorial`, `gcd`, `lcm`

#### 字符串处理
- **格式化**: `capitalize`, `title`, `upper`, `lower`, `swapcase`, `reverse`, `truncate`, `strip`, `lstrip`, `rstrip`, `camel_to_snake`, `snake_to_camel`, `mask`, `format_size`, `format_number`, `format_datetime`
- **验证**: `is_empty`, `is_numeric`, `is_integer`, `is_alpha`, `is_alphanumeric`, `is_email`, `is_phone_cn`, `is_id_card_cn`, `is_url`, `is_ip`, `is_hex_color`, `is_date`, `is_chinese`, `contains_chinese`, `length_between`, `matches`

#### 日期时间
- **获取时间**: `now`, `today`, `timestamp`, `timestamp_ms`
- **转换**: `from_timestamp`, `parse`, `format`
- **计算**: `add_days`, `add_hours`, `add_minutes`, `diff_days`, `diff_seconds`
- **判断**: `is_weekend`, `is_weekday`
- **工具**: `get_age`, `get_quarter`, `get_week_of_year`, `get_day_of_year`

#### 文件操作
- **读写**: `read_text`, `write_text`, `read_lines`, `write_lines`, `read_json`, `write_json`
- **信息**: `exists`, `is_file`, `is_dir`, `get_size`, `get_extension`, `get_filename`, `get_basename`, `get_parent`
- **路径**: `join_path`
- **操作**: `create_dir`, `delete_file`, `delete_dir`, `copy_file`, `copy_dir`, `move`, `rename`
- **列表**: `list_files`, `list_dirs`
- **哈希**: `get_md5`, `get_sha256`

---

### 🔗 相关链接

- [PyPI项目主页](https://pypi.org/project/metax/)
- [GitHub仓库](https://github.com/ACANX/MetaX)
- [问题反馈](https://github.com/ACANX/MetaX/issues)

---

### 📝 更新日志

#### v0.1.2 (2024-01-15)
- ✨ 新增高级数学运算（幂、开方、三角函数、对数等）
- ✨ 新增字符串格式化工具
- ✨ 新增字符串验证工具
- ✨ 新增日期时间工具
- ✨ 新增文件操作工具
- 🐛 修复除法运算的零除异常处理
- 📝 完善文档和使用示例

#### v0.1.1 (2024-01-15)
- ✨ 新增基础数学运算（加减乘除）
- 🎉 初始版本发布

#### v0.1.0 (2024-01-15)
- 🎉 项目初始化
