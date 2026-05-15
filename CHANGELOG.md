# 更新日志

本文档记录MetaX项目的所有重要更改。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

### 计划新增
- 🔖 更多字符串处理工具
- 🔖 网络请求工具
- 🔖 数据加密工具

---

## [0.1.2] - 2026-05-15

### 新增

#### 数学运算模块
- ✨ 新增高级数学运算功能
  - `power()` - 幂运算
  - `sqrt()` - 平方根
  - `cbrt()` - 立方根
  - `sin()`, `cos()`, `tan()` - 三角函数
  - `log()`, `log10()`, `log2()` - 对数函数
  - `abs()` - 绝对值
  - `round()`, `floor()`, `ceil()` - 取整函数
  - `factorial()` - 阶乘
  - `gcd()`, `lcm()` - 最大公约数、最小公倍数

#### 字符串处理模块
- ✨ 新增字符串格式化工具
  - `capitalize()`, `title()`, `upper()`, `lower()`, `swapcase()` - 大小写转换
  - `reverse()` - 字符串反转
  - `truncate()` - 字符串截断
  - `strip()`, `lstrip()`, `rstrip()` - 去除空白
  - `camel_to_snake()`, `snake_to_camel()` - 命名转换
  - `mask()` - 字符串脱敏
  - `format_size()` - 文件大小格式化
  - `format_number()` - 数字格式化（千分位）
  - `format_datetime()` - 日期时间格式化

- ✨ 新增字符串验证工具
  - `is_empty()` - 空字符串判断
  - `is_numeric()`, `is_integer()` - 数字验证
  - `is_alpha()`, `is_alphanumeric()` - 字母验证
  - `is_email()` - 邮箱验证
  - `is_phone_cn()` - 中国大陆手机号验证
  - `is_id_card_cn()` - 身份证号验证
  - `is_url()` - URL验证
  - `is_ip()` - IP地址验证
  - `is_hex_color()` - 十六进制颜色验证
  - `is_date()` - 日期验证
  - `is_chinese()`, `contains_chinese()` - 中文验证
  - `length_between()` - 长度范围验证
  - `matches()` - 正则匹配

#### 日期时间模块
- ✨ 新增日期时间工具
  - `now()`, `today()` - 获取当前时间/日期
  - `timestamp()`, `timestamp_ms()` - 获取时间戳
  - `from_timestamp()` - 时间戳转换
  - `parse()`, `format()` - 解析和格式化
  - `add_days()`, `add_hours()`, `add_minutes()` - 时间加减
  - `diff_days()`, `diff_seconds()` - 时间差计算
  - `is_weekend()`, `is_weekday()` - 周末/工作日判断
  - `get_age()` - 年龄计算
  - `get_quarter()` - 季度获取
  - `get_week_of_year()`, `get_day_of_year()` - 年中第几周/天

#### 文件操作模块
- ✨ 新增文件操作工具
  - `read_text()`, `write_text()` - 文本文件读写
  - `read_lines()`, `write_lines()` - 按行读写
  - `read_json()`, `write_json()` - JSON文件读写
  - `exists()`, `is_file()`, `is_dir()` - 文件/目录判断
  - `get_size()` - 获取文件大小
  - `get_extension()`, `get_filename()`, `get_basename()` - 文件信息获取
  - `get_parent()`, `join_path()` - 路径操作
  - `create_dir()` - 创建目录
  - `delete_file()`, `delete_dir()` - 删除文件/目录
  - `copy_file()`, `copy_dir()` - 复制文件/目录
  - `move()`, `rename()` - 移动/重命名
  - `list_files()`, `list_dirs()` - 列出文件/目录
  - `get_md5()`, `get_sha256()` - 文件哈希计算

### 优化
- 📝 完善项目文档结构
  - 新增 `Docs/Deploy.md` - 部署说明文档
  - 新增 `Docs/Usage.md` - 使用指南文档
  - 新增 `Docs/Update.md` - 更新升级流程文档
  - 新增 `Docs/README.md` - 文档入口
- 📝 完善函数文档字符串（docstring）
- ⚡️ 优化项目结构，按模块组织代码

### 文档
- 📚 新增完整的部署说明文档
- 📚 新增详细的使用指南和示例
- 📚 新增更新升级流程规范
- 📚 新增文档导航入口

---

## [0.1.1] - 2026-01-15

### 新增
- ✨ 新增基础数学运算功能
  - `add()` - 加法运算
  - `subtract()` - 减法运算
  - `multiply()` - 乘法运算
  - `divide()` - 除法运算（含零除异常处理）
- ✨ 新增问候函数 `hello()`
- 📝 新增项目基本信息
  - 版本号管理
  - 作者信息
  - 许可证（MIT）

### 修复
- 🐛 修复除法运算的零除异常处理

### 文档
- 📚 创建基本项目结构文档

---

## [0.1.0] - 2026-05-15

### 新增
- 🎉 项目初始化
- 📦 创建基本项目结构
- 📝 创建 README.md 项目说明文档
- 📝 创建 LICENSE 许可证文件
- 🔧 配置 pyproject.toml 打包文件
- 🚀 首次发布到 PyPI

---

## 版本说明

### 版本号规范

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **主版本号（Major）**：不兼容的API修改
- **次版本号（Minor）**：向下兼容的功能新增
- **修订号（Patch）**：向下兼容的问题修复

### 更新类型图标

- 🎉 `新增` - 新功能
- 🐛 `修复` - Bug修复
- 🔖 `变更` - 功能变更
- 🚫 `移除` - 功能移除
- 🔒 `安全` - 安全相关
- 📝 `文档` - 文档更新
- 🔧 `配置` - 配置变更
- ⚡️ `优化` - 性能优化
- 🎨 `重构` - 代码重构

---

## 贡献者

感谢以下贡献者对本项目的贡献：

- **ACANX** - *项目创建者和主要维护者* - [ACANX](https://github.com/ACANX)

---

## 链接

- [PyPI项目主页](https://pypi.org/project/metax/)
- [TestPyPI项目主页](https://test.pypi.org/project/metax/)
- [GitHub仓库](https://github.com/ACANX/MetaX)
- [问题反馈](https://github.com/ACANX/MetaX/issues)
- [更新日志](CHANGELOG.md)
- [使用指南](Docs/Usage.md)
- [部署说明](Docs/Deploy.md)
- [更新流程](Docs/Update.md)

---

**最后更新**：2026-05-15
