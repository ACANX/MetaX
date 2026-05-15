## 部署说明


---

### 📦 1. 准备项目结构

新建一个文件夹作为项目根目录，结构如下：

```
MetaX/
├── metax/
│   ├── __init__.py
│   ├── base/
│   │   ├── __init__.py
│   │   └── math/
│   │       ├── __init__.py
│   │       ├── basic.py
│   │       └── advanced.py
│   └── util/
│       ├── __init__.py
│       ├── string/
│       │   ├── __init__.py
│       │   ├── format.py
│       │   └── validate.py
│       ├── datetime/
│       │   └── __init__.py
│       └── file/
│           └── __init__.py
├── tests/
│   └── test_math.py
├── pyproject.toml
├── LICENSE
└── README.md
```

*   `MetaX/`（外层）是项目根目录。
*   `metax/`（内层）是包目录，里面必须有一个 `__init__.py`。
*   `pyproject.toml` 是打包配置文件。
*   `LICENSE` 是许可证文件（MIT）。
*   `README.md` 是项目说明文档。

---

### ⚙️ 2. 配置打包信息（重要）

在根目录创建 `pyproject.toml`，内容如下：

```toml
[build-system]
requires = ["setuptools>=78.1.1", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "metax"
version = "0.1.2"
description = "MetaOpen Python Language lib package"
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
license-files = ["LICENSE"]
authors = [
    {name = "ACANX", email = "acanx@qq.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

[tool.setuptools]
packages = ["metax"]
```

#### ⚠️ 重要说明（踩坑记录）

1. **setuptools版本建议≥78.1.1**
   - `>=78.1.1` 兼容新版 Metadata-Version 2.4，配合 `packaging>=26.2` 即可通过 twine 校验
   - 不要锁定旧版 `setuptools==69.0.0`（过时且缺少新特性）

2. **license 配置使用 SPDX 表达式**
   - 推荐格式：`license = "MIT"`（SPDX 表达式字符串，参见 [PEP 639](https://peps.python.org/pep-0639/)）
   - 旧格式 `license = {file = "LICENSE"}` 已弃用，setuptools 77+ 会打印 DeprecationWarning
   - 可使用 `license-files = ["LICENSE"]` 显式声明许可证文件

3. **build-backend必须使用setuptools.build_meta**
   - 不要使用 `setuptools.backends._legacy:_Backend`（已废弃）
   - 不要使用 `setuptools.build_meta:__legacy__`（有兼容性问题）

4. **明确指定packages**
   - 使用 `[tool.setuptools]` 配置明确指定包名
   - 避免自动发现时包含不需要的目录（如Docs目录）

---

### 🛠️ 3. 安装打包工具

确保你已安装最新版的 `build` 和 `twine`：

```bash
# 使用Python3安装（重要！）
python3 -m pip install --upgrade build twine
```

#### ⚠️ 重要说明（踩坑记录）

**必须使用 `python3 -m` 方式调用工具**

如果你的系统同时安装了Python 2.7和Python 3：
- `twine` 命令可能指向Python 2.7的旧版本（如1.15.0）
- `python3 -m twine` 会使用Python 3的新版本（如6.2.0）

验证twine版本：
```bash
# 错误方式（可能使用Python 2.7的旧版本）
twine --version

# 正确方式（使用Python 3的新版本）
python3 -m twine --version
```

---

### 🔨 4. 构建发布包

在根目录（包含 `pyproject.toml` 的那个目录）下执行：

```bash
# 清理旧的构建文件（推荐）
Remove-Item -Recurse -Force dist, build, metax.egg-info -ErrorAction SilentlyContinue

# 构建新版本
python3 -m build
```

运行后会在 `dist/` 文件夹中生成两个文件：
*   `metax-0.1.2.tar.gz`（源码包）
*   `metax-0.1.2-py3-none-any.whl`（wheel包）

#### 验证构建结果

```bash
python3 -m twine check dist/*
```

如果输出 `PASSED`，说明包的元数据格式正确。

---

### 📝 5. 配置PyPI认证

#### 创建API Token

1. **TestPyPI（测试环境）**
   - 访问：https://test.pypi.org/manage/account/token/
   - 创建API Token，复制token值（以 `pypi-` 开头）

2. **PyPI（正式环境）**
   - 访问：https://pypi.org/manage/account/token/
   - 创建API Token，复制token值（以 `pypi-` 开头）

#### 配置.pypirc文件

在用户目录下创建 `.pypirc` 文件：

**Windows系统**：`C:\Users\你的用户名\.pypirc`

**Linux/Mac系统**：`~/.pypirc`

文件内容如下：

```ini
[testpypi]
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZw...（你的TestPyPI Token）

[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmc...（你的PyPI Token）
```

#### ⚠️ 安全提示

- Token值以 `pypi-` 开头，包含完整的token字符串
- 用户名固定为 `__token__`（注意是双下划线）
- 不要将 `.pypirc` 文件提交到Git仓库

---

### 📤 6. 上传到TestPyPI（测试环境）

**推荐先上传到TestPyPI测试**

```bash
python3 -m twine upload --repository testpypi dist/*
```

#### ⚠️ 常见错误

**错误1：HTTPError: 400 Bad Request**
- 原因：版本号已存在
- 解决：更新 `pyproject.toml` 中的 `version` 字段

**错误2：twine check 元数据验证失败**
- 原因：`packaging` 库版本过低（< 26.x），不认识 Metadata-Version 2.4 的 `License-File` 字段
- 解决：升级 `packaging` 到最新版（`python3 -m pip install --upgrade packaging`），而非降级 setuptools

#### 验证安装

```bash
# 安装测试
python3 -m pip install --index-url https://test.pypi.org/simple/ metax

# 测试功能
python3 -c "import metax; print(metax.hello('TestPyPI'))"
```

---

### 📤 7. 上传到PyPI（正式环境）

确认TestPyPI测试通过后，上传到正式环境：

```bash
python3 -m twine upload dist/*
```

上传成功后会显示：
```
View at:
https://pypi.org/project/metax/0.1.2/
```

#### 验证安装

```bash
# 安装
pip install metax

# 测试功能
python3 -c "import metax; print(metax.hello('PyPI'))"
```

---

### 🧪 8. 完整测试命令

一条命令完成升级安装和功能测试：

```bash
python3 -m pip install metax --upgrade --quiet; python3 -c "import metax; print('版本:', metax.__version__); print('加法:', metax.add(10, 5)); print('幂运算:', metax.power(2, 3)); print('邮箱验证:', metax.is_email('test@example.com')); print('当前时间:', metax.now()); print('路径拼接:', metax.join_path('D:', 'test', 'file.txt'))"
```

---

### 🔁 9. 更新版本流程

每次更新库的完整流程：

1. **修改代码** - 添加新功能或修复bug

2. **更新版本号** - 在以下两个文件中修改：
   - `pyproject.toml` 中的 `version` 字段
   - `metax/__init__.py` 中的 `__version__` 变量

3. **清理并构建**
   ```bash
   Remove-Item -Recurse -Force dist, build, metax.egg-info -ErrorAction SilentlyContinue
   python3 -m build
   ```

4. **验证包**
   ```bash
   python3 -m twine check dist/*
   ```

5. **上传到TestPyPI测试**
   ```bash
   python3 -m twine upload --repository testpypi dist/*
   ```

6. **测试通过后上传到正式PyPI**
   ```bash
   python3 -m twine upload dist/*
   ```

---

### 📋 版本号规范

遵循语义化版本规范（Semantic Versioning）：

- **主版本号（Major）**：不兼容的API修改
- **次版本号（Minor）**：向下兼容的功能新增
- **修订号（Patch）**：向下兼容的问题修复

示例：
- `0.1.0` - 初始版本
- `0.1.1` - 修复bug
- `0.1.2` - 新增功能（向下兼容）
- `1.0.0` - 正式发布版本

---

### 🚨 常见问题汇总

#### Q1: twine check报错 "Invalid distribution metadata"
**原因**：`packaging` 库版本过低（< 26.x），不认识 Metadata-Version 2.4 的 `License-File` 字段
**解决**：升级 `packaging` 库：`python3 -m pip install --upgrade packaging`

#### Q2: twine命令找不到或版本过低
**原因**：系统同时安装了Python 2.7和Python 3
**解决**：使用 `python3 -m twine` 代替 `twine`

#### Q3: 上传失败 400 Bad Request
**原因**：版本号已存在于PyPI
**解决**：更新版本号后重新构建

#### Q4: 包含了不需要的目录（如Docs）
**原因**：setuptools自动发现机制
**解决**：在 `pyproject.toml` 中明确指定 `[tool.setuptools] packages = ["metax"]`

#### Q5: PowerShell中&&不支持
**原因**：PowerShell语法不同于Bash
**解决**：使用分号 `;` 代替 `&&`

---

### 📚 参考资源

- [Python Packaging User Guide](https://packaging.python.org/)
- [setuptools文档](https://setuptools.pypa.io/)
- [twine文档](https://twine.readthedocs.io/)
- [PyPI官网](https://pypi.org/)
- [TestPyPI官网](https://test.pypi.org/)
