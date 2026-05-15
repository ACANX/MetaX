## 更新升级流程规范


---

### 📋 目录

1. [修改代码](#1-修改代码)
2. [单元测试](#2-单元测试)
3. [更新版本号](#3-更新版本号)
4. [构建发布包](#4-构建发布包)
5. [发布到测试环境](#5-发布到测试环境)
6. [验证测试包](#6-验证测试包)
7. [发布到正式环境](#7-发布到正式环境)
8. [测试正式包](#8-测试正式包)
9. [常见问题](#9-常见问题)

---

### 1. 修改代码

#### 1.1 开发流程

**步骤1：创建功能分支**

```bash
# 从main分支创建新的功能分支
git checkout main
git pull origin main
git checkout -b feature/new-function-name
```

**步骤2：修改代码**

按照Python最佳实践添加新功能：

```python
# 在对应的模块文件中添加新函数
# 例如：metax/base/math/basic.py

def new_function(a: float, b: float) -> float:
    """新功能描述
    
    详细说明函数的功能
    
    Args:
        a: 参数a说明
        b: 参数b说明
    
    Returns:
        返回值说明
    
    Raises:
        ExceptionType: 异常情况说明
    
    Example:
        >>> new_function(10, 5)
        15
    """
    # 函数实现
    return a + b
```

**步骤3：更新模块导出**

在模块的`__init__.py`中导出新函数：

```python
# metax/base/math/__init__.py

from metax.base.math.basic import add, subtract, multiply, divide, new_function

__all__ = ['add', 'subtract', 'multiply', 'divide', 'new_function']
```

**步骤4：更新包入口导出**

在主入口文件中导出新函数：

```python
# metax/__init__.py

from metax.base.math.basic import add, subtract, multiply, divide, new_function

__all__ = [
    'hello',
    'add', 'subtract', 'multiply', 'divide', 'new_function',
    # ... 其他函数
]
```

#### 1.2 代码规范

- ✅ 所有函数必须有类型注解
- ✅ 所有函数必须有文档字符串（docstring）
- ✅ 文档字符串包含：描述、Args、Returns、Raises（如有）、Example（推荐）
- ✅ 函数命名使用小写+下划线：`function_name`
- ✅ 类命名使用大驼峰：`ClassName`
- ✅ 常量命名使用大写+下划线：`MAX_SIZE`

---

### 2. 单元测试

#### 2.1 创建测试文件

在`tests/`目录下创建测试文件：

```python
# tests/test_math.py

import sys
sys.path.insert(0, 'D:\\Code\\PyCode\\MetaX')

from metax.base.math import basic


def test_add():
    """测试加法"""
    assert basic.add(10, 5) == 15
    assert basic.add(-1, 1) == 0
    assert basic.add(0, 0) == 0
    print("✓ 加法测试通过")


def test_subtract():
    """测试减法"""
    assert basic.subtract(10, 5) == 5
    assert basic.subtract(5, 10) == -5
    assert basic.subtract(0, 0) == 0
    print("✓ 减法测试通过")


def test_multiply():
    """测试乘法"""
    assert basic.multiply(10, 5) == 50
    assert basic.multiply(-2, 3) == -6
    assert basic.multiply(0, 100) == 0
    print("✓ 乘法测试通过")


def test_divide():
    """测试除法"""
    assert basic.divide(10, 5) == 2.0
    assert basic.divide(7, 2) == 3.5
    
    # 测试异常
    try:
        basic.divide(10, 0)
        assert False, "应该抛出ZeroDivisionError"
    except ZeroDivisionError:
        pass
    
    print("✓ 除法测试通过")


def test_new_function():
    """测试新功能"""
    assert basic.new_function(10, 5) == 15
    assert basic.new_function(0, 0) == 0
    print("✓ 新功能测试通过")


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_new_function()
    print("\n✅ 所有测试通过！")
```

#### 2.2 运行测试

**方式1：直接运行测试文件**

```bash
python3 tests/test_math.py
```

**方式2：使用pytest（推荐）**

```bash
# 安装pytest
pip install pytest

# 运行所有测试
pytest tests/

# 运行特定测试文件
pytest tests/test_math.py

# 运行特定测试函数
pytest tests/test_math.py::test_add

# 显示详细输出
pytest tests/ -v

# 显示打印输出
pytest tests/ -s
```

#### 2.3 测试覆盖率

使用pytest-cov检查测试覆盖率：

```bash
# 安装pytest-cov
pip install pytest-cov

# 运行测试并生成覆盖率报告
pytest tests/ --cov=metax --cov-report=html

# 查看HTML报告
# 打开 htmlcov/index.html
```

#### 2.4 测试规范

- ✅ 每个函数至少有一个测试用例
- ✅ 测试正常情况
- ✅ 测试边界情况
- ✅ 测试异常情况
- ✅ 测试文件命名：`test_*.py`
- ✅ 测试函数命名：`test_*`

---

### 3. 更新版本号

#### 3.1 版本号规范

遵循语义化版本规范（Semantic Versioning）：

```
主版本号.次版本号.修订号
Major.Minor.Patch
```

- **主版本号（Major）**：不兼容的API修改
- **次版本号（Minor）**：向下兼容的功能新增（0.x版本常用）
- **修订号（Patch）**：向下兼容的问题修复

示例：
- `0.1.0` - 初始版本
- `0.1.1` - 修复bug
- `0.1.2` - 新增功能（向下兼容）
- `1.0.0` - 正式发布版本

#### 3.2 更新版本号位置

需要同时更新以下两个文件：

**文件1：pyproject.toml**

```toml
[project]
name = "metax"
version = "0.1.4"  # 更新这里
```

**文件2：metax/__init__.py**

```python
__version__ = "0.1.4"  # 更新这里
```

#### 3.3 版本号更新命令

使用命令快速更新：

```bash
# PowerShell
# 更新pyproject.toml
(Get-Content pyproject.toml) -replace 'version = "0.1.3"', 'version = "0.1.4"' | Set-Content pyproject.toml

# 更新__init__.py
(Get-Content metax/__init__.py) -replace '__version__ = "0.1.3"', '__version__ = "0.1.4"' | Set-Content metax/__init__.py
```

---

### 4. 构建发布包

#### 4.1 清理旧文件

构建前清理旧的构建文件：

```bash
# PowerShell
Remove-Item -Recurse -Force dist, build, metax.egg-info -ErrorAction SilentlyContinue
```

#### 4.2 构建新版本

```bash
python3 -m build
```

构建成功后会显示：

```
Successfully built metax-0.1.4.tar.gz and metax-0.1.4-py3-none-any.whl
```

#### 4.3 验证构建结果

```bash
# 检查包的元数据
python3 -m twine check dist/*

# 查看生成的文件
ls dist/
```

输出应该是：

```
metax-0.1.4-py3-none-any.whl
metax-0.1.4.tar.gz
```

---

### 5. 发布到测试环境

#### 5.1 上传到TestPyPI

```bash
python3 -m twine upload --repository testpypi dist/*
```

成功输出：

```
Uploading distributions to https://test.pypi.org/legacy/
Uploading metax-0.1.4-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━ 25.1/25.1 kB • 00:00 • 5.3 MB/s
Uploading metax-0.1.4.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━ 25.3/25.3 kB • 00:00 • 6.9 MB/s

View at:
https://test.pypi.org/project/metax/0.1.4/
```

#### 5.2 常见错误处理

**错误1：HTTPError: 400 Bad Request**

```
ERROR HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
Bad Request
```

**原因**：版本号已存在于TestPyPI

**解决**：更新版本号后重新构建

**错误2：Invalid distribution metadata**

```
ERROR InvalidDistribution: Invalid distribution metadata
```

**原因**：setuptools版本过高

**解决**：使用 `setuptools==69.0.0`

---

### 6. 验证测试包

#### 6.1 安装测试包

```bash
# 从TestPyPI安装
python3 -m pip install --index-url https://test.pypi.org/simple/ metax --upgrade
```

#### 6.2 验证版本

```bash
python3 -c "import metax; print('版本:', metax.__version__)"
```

输出：

```
版本: 0.1.4
```

#### 6.3 功能测试

**快速测试所有功能**：

```bash
python3 -c "import metax; print('=== 数学运算 ==='); print('加法:', metax.add(10, 5)); print('幂运算:', metax.power(2, 3)); print('=== 字符串处理 ==='); print('反转:', metax.reverse('hello')); print('邮箱验证:', metax.is_email('test@example.com')); print('=== 日期时间 ==='); print('当前时间:', metax.now()); print('=== 文件操作 ==='); print('路径拼接:', metax.join_path('D:', 'test', 'file.txt'))"
```

**测试新功能**：

```bash
python3 -c "import metax; print('新功能:', metax.new_function(10, 5))"
```

#### 6.4 运行单元测试

```bash
# 使用已安装的包运行测试
pytest tests/ -v
```

---

### 7. 发布到正式环境

#### 7.1 确认测试通过

确保以下检查全部通过：

- ✅ TestPyPI安装成功
- ✅ 版本号正确
- ✅ 所有功能正常
- ✅ 新功能测试通过
- ✅ 单元测试全部通过

#### 7.2 上传到PyPI

```bash
python3 -m twine upload dist/*
```

成功输出：

```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading metax-0.1.4-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━ 25.1/25.1 kB • 00:00 • 4.9 MB/s
Uploading metax-0.1.4.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━ 25.3/25.3 kB • 00:00 • 7.3 MB/s

View at:
https://pypi.org/project/metax/0.1.4/
```

#### 7.3 查看发布结果

访问PyPI项目页面：

```
https://pypi.org/project/metax/0.1.4/
```

---

### 8. 测试正式包

#### 8.1 卸载测试包

```bash
pip uninstall metax -y
```

#### 8.2 安装正式包

```bash
pip install metax
```

#### 8.3 验证版本

```bash
python3 -c "import metax; print('版本:', metax.__version__)"
```

#### 8.4 完整功能测试

```bash
python3 -m pip install metax --upgrade --quiet; python3 -c "import metax; print('=== 版本验证 ==='); print('版本:', metax.__version__); print('\n=== 数学运算 ==='); print('加法:', metax.add(10, 5)); print('减法:', metax.subtract(10, 5)); print('乘法:', metax.multiply(10, 5)); print('除法:', metax.divide(10, 5)); print('幂运算:', metax.power(2, 3)); print('平方根:', metax.sqrt(16)); print('\n=== 字符串处理 ==='); print('反转:', metax.reverse('hello')); print('邮箱验证:', metax.is_email('test@example.com')); print('手机号验证:', metax.is_phone_cn('13812345678')); print('\n=== 日期时间 ==='); print('当前时间:', metax.now()); print('时间戳:', metax.timestamp()); print('\n=== 文件操作 ==='); print('路径拼接:', metax.join_path('D:', 'test', 'file.txt')); print('文件大小格式化:', metax.format_size(1024000))"
```

#### 8.5 运行单元测试

```bash
pytest tests/ -v
```

---

### 9. 常见问题

#### Q1: 版本号已存在错误

**错误信息**：

```
ERROR HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
Bad Request
```

**原因**：PyPI不允许覆盖已发布的版本

**解决方案**：

1. 更新版本号（`pyproject.toml` 和 `metax/__init__.py`）
2. 清理旧的构建文件
3. 重新构建
4. 重新上传

#### Q2: 元数据验证失败

**错误信息**：

```
ERROR InvalidDistribution: Invalid distribution metadata: unrecognized or malformed field 'license-file'
```

**原因**：`packaging` 库版本过低（< 26.x），不认识 Metadata-Version 2.4 的 `License-File` 字段

**解决方案**：

升级 `packaging` 库（而非降级 setuptools）：

```bash
python3 -m pip install --upgrade packaging
```

#### Q3: twine版本过低

**错误信息**：

```
twine version 1.15.0
```

**原因**：系统同时安装了Python 2.7和Python 3

**解决方案**：

使用 `python3 -m twine` 代替 `twine`：

```bash
# 错误方式
twine upload dist/*

# 正确方式
python3 -m twine upload dist/*
```

#### Q4: 测试包无法安装

**错误信息**：

```
ERROR: Could not find a version that satisfies the requirement metax
```

**原因**：使用了错误的pip命令

**解决方案**：

使用Python 3的pip：

```bash
# 错误方式
pip install --index-url https://test.pypi.org/simple/ metax

# 正确方式
python3 -m pip install --index-url https://test.pypi.org/simple/ metax
```

#### Q5: 包含了不需要的目录

**错误信息**：

```
error: Multiple top-level packages discovered in a flat-layout: ['Docs', 'metax'].
```

**原因**：setuptools自动发现机制包含了不需要的目录

**解决方案**：

在 `pyproject.toml` 中明确指定包：

```toml
[tool.setuptools]
packages = ["metax"]
```

---

### 📋 完整流程检查清单

#### 开发阶段
- [ ] 创建功能分支
- [ ] 编写代码（遵循规范）
- [ ] 更新模块导出
- [ ] 更新包入口导出
- [ ] 编写单元测试
- [ ] 运行单元测试通过

#### 构建阶段
- [ ] 更新版本号（两个文件）
- [ ] 清理旧的构建文件
- [ ] 构建新版本
- [ ] 验证构建结果（twine check）

#### 测试环境
- [ ] 上传到TestPyPI
- [ ] 从TestPyPI安装
- [ ] 验证版本号
- [ ] 测试所有功能
- [ ] 测试新功能
- [ ] 运行单元测试

#### 正式环境
- [ ] 确认测试全部通过
- [ ] 上传到PyPI
- [ ] 卸载测试包
- [ ] 安装正式包
- [ ] 验证版本号
- [ ] 完整功能测试
- [ ] 运行单元测试

#### 发布后
- [ ] 合并代码到main分支
- [ ] 创建Git标签
- [ ] 更新更新日志
- [ ] 通知用户更新

---

### 🔄 快速更新脚本

创建一个PowerShell脚本 `update.ps1` 自动化更新流程：

```powershell
# update.ps1 - MetaX更新脚本

param(
    [Parameter(Mandatory=$true)]
    [string]$Version,
    
    [switch]$SkipTest,
    [switch]$SkipBuild
)

# 颜色输出函数
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

# 1. 更新版本号
Write-ColorOutput Green "=== 步骤1: 更新版本号到 $Version ==="
(Get-Content pyproject.toml) -replace 'version = ".*"', "version = `"$Version`"" | Set-Content pyproject.toml
(Get-Content metax/__init__.py) -replace '__version__ = ".*"', "__version__ = `"$Version`"" | Set-Content metax/__init__.py
Write-ColorOutput Green "✓ 版本号已更新"

# 2. 运行测试
if (-not $SkipTest) {
    Write-ColorOutput Green "`n=== 步骤2: 运行单元测试 ==="
    pytest tests/ -v
    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput Red "✗ 测试失败，请检查代码"
        exit 1
    }
    Write-ColorOutput Green "✓ 所有测试通过"
}

# 3. 构建发布包
if (-not $SkipBuild) {
    Write-ColorOutput Green "`n=== 步骤3: 构建发布包 ==="
    Remove-Item -Recurse -Force dist, build, metax.egg-info -ErrorAction SilentlyContinue
    python3 -m build
    Write-ColorOutput Green "✓ 构建完成"
    
    # 验证构建结果
    Write-ColorOutput Green "`n=== 步骤4: 验证构建结果 ==="
    python3 -m twine check dist/*
    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput Red "✗ 构建验证失败"
        exit 1
    }
    Write-ColorOutput Green "✓ 构建验证通过"
}

Write-ColorOutput Green "`n=== 准备就绪 ==="
Write-ColorOutput Yellow "下一步操作："
Write-ColorOutput Yellow "1. 上传到TestPyPI: python3 -m twine upload --repository testpypi dist/*"
Write-ColorOutput Yellow "2. 测试通过后上传到PyPI: python3 -m twine upload dist/*"
```

**使用方法**：

```powershell
# 更新到0.1.4版本
.\update.ps1 -Version "0.1.4"

# 跳过测试
.\update.ps1 -Version "0.1.4" -SkipTest

# 跳过构建
.\update.ps1 -Version "0.1.4" -SkipBuild
```

---

### 📝 更新日志模板

每次更新后，在项目根目录的`CHANGELOG.md`中记录：

```markdown
# 更新日志

## [0.1.4] - 2026-05-15

### 新增
- ✨ 新增xxx功能
- ✨ 新增yyy功能

### 修复
- 🐛 修复xxx问题
- 🐛 修复yyy问题

### 优化
- ⚡️ 优化xxx性能
- 📝 完善xxx文档

### 变更
- ♻️ 重构xxx模块
- 🔥 移除xxx功能

## [0.1.2] - 2024-01-15

### 新增
- ✨ 新增高级数学运算
- ✨ 新增字符串处理工具
- ✨ 新增日期时间工具
- ✨ 新增文件操作工具
```

---

### 🔗 相关文档

- [部署说明](Deploy.md)
- [使用指南](Usage.md)
- [PyPI官网](https://pypi.org/)
- [TestPyPI官网](https://test.pypi.org/)
