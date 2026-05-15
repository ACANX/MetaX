# MetaX

[![PyPI version](https://badge.fury.io/py/metax.svg)](https://badge.fury.io/py/metax)
[![Python](https://img.shields.io/pypi/pyversions/metax.svg)](https://pypi.org/project/metax/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[English](README.md) | 中文

---

**MetaX** 是一个功能丰富的Python工具库，提供数学运算、字符串处理、日期时间、文件操作等常用工具函数，帮助开发者提高开发效率。

### 📖 项目定位

MetaX致力于成为Python开发者的得力助手，提供：

- **🔢 数学运算** - 基础运算、高级数学函数、数论工具
- **📝 字符串处理** - 格式化、验证、转换工具
- **⏰ 日期时间** - 时间获取、计算、格式化工具
- **📁 文件操作** - 文件读写、路径操作、哈希计算

所有函数都经过精心设计，提供完整的类型注解和文档字符串，支持IDE自动提示，开箱即用。

### 🚀 安装

#### 使用pip安装

```bash
pip install metax
```

#### 升级到最新版本

```bash
pip install metax --upgrade
```

#### 从TestPyPI安装（测试版本）

```bash
pip install --index-url https://test.pypi.org/simple/ metax
```

### 💡 快速开始

#### 基础示例

```python
import metax

# 问候函数
print(metax.hello("世界"))  # 输出: 你好, 世界!
```

#### 数学运算

```python
import metax

# 基础运算
print(metax.add(10, 5))        # 加法: 15
print(metax.subtract(10, 5))   # 减法: 5
print(metax.multiply(10, 5))   # 乘法: 50
print(metax.divide(10, 5))     # 除法: 2.0

# 高级运算
print(metax.power(2, 3))       # 幂运算: 8.0
print(metax.sqrt(16))          # 平方根: 4.0
print(metax.factorial(5))      # 阶乘: 120
```

#### 字符串处理

```python
import metax

# 格式化
print(metax.reverse("hello"))           # 反转: olleh
print(metax.mask("13812345678", 3, 4))  # 脱敏: 138****5678
print(metax.format_size(1024000))       # 文件大小: 1000.00 KB

# 验证
print(metax.is_email("test@example.com"))   # 邮箱验证: True
print(metax.is_phone_cn("13812345678"))     # 手机号验证: True
print(metax.is_url("https://example.com"))  # URL验证: True
```

#### 日期时间

```python
import metax

print(metax.now())           # 当前时间: 2026-05-15 10:30:45
print(metax.timestamp())     # 时间戳: 1705285845
print(metax.today())         # 今天日期: 2026-05-15
```

#### 文件操作

```python
import metax

# 文件读写
metax.write_text("test.txt", "Hello, MetaX!")
content = metax.read_text("test.txt")

# 路径操作
path = metax.join_path("D:", "test", "file.txt")
print(metax.get_extension("test.txt"))  # 扩展名: .txt
```

### 📚 文档

#### 文档入口

- **[📖 文档中心](Docs/README.md)** - 完整文档导航

#### 详细文档

- **[🚀 部署说明](Docs/Deploy.md)** - 如何发布PyPI包
- **[📖 使用指南](Docs/Usage.md)** - 详细的使用说明和API文档
- **[🔄 更新流程](Docs/Update.md)** - 版本更新和发布流程

#### 更新日志

- **[📝 CHANGELOG.md](CHANGELOG.md)** - 版本更新历史

### 🔗 重要链接

#### PyPI

- **[PyPI项目主页](https://pypi.org/project/metax/)** - 正式发布版本
- **[TestPyPI项目主页](https://test.pypi.org/project/metax/)** - 测试版本

#### GitHub

- **[GitHub仓库](https://github.com/ACANX/MetaX)** - 源代码仓库
- **[问题反馈](https://github.com/ACANX/MetaX/issues)** - 提交Bug或功能请求

### 📦 功能概览

| 模块 | 功能 | 函数数量 |
|------|------|----------|
| 数学运算 | 基础运算、高级运算、数论函数 | 17个 |
| 字符串处理 | 格式化、验证 | 26个 |
| 日期时间 | 时间获取、计算、判断 | 17个 |
| 文件操作 | 读写、路径、哈希 | 22个 |

**总计：82+个实用函数**

### 🎯 适用场景

- **数据处理** - 数学计算、字符串处理
- **表单验证** - 邮箱、手机号、身份证验证
- **日志处理** - 时间格式化、文件操作
- **工具开发** - 快速构建命令行工具
- **自动化脚本** - 文件处理、数据转换

### 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

#### 贡献流程

1. Fork 项目仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

详细流程请参考 [更新流程文档](Docs/Update.md)

### 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

### 📊 版本信息

- **当前版本**：0.1.2
- **Python版本**：>= 3.8

### 🌟 Star History

如果这个项目对你有帮助，请给一个 ⭐️ Star 支持一下！

---

**Made with ❤️ by ACANX**
