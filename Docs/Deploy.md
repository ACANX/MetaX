## 部署说明


---

### 📦 1. 准备项目结构

新建一个文件夹作为项目根目录，结构如下：

```
MetaX/
├── metax/
│   └── __init__.py
└── pyproject.toml
```

*   `MetaX/`（外层）是项目根目录。
*   `metax/`（内层）是包目录，里面必须有一个 `__init__.py`。
*   `pyproject.toml` 是打包配置文件。

---

### ✍️ 2. 编写代码

在 `metax/__init__.py` 中写一个最简单的函数：

```python
def hello(name: str = "世界") -> str:
    """返回一个问候语"""
    return f"你好, {name}!"
```

---

### ⚙️ 3. 配置打包信息

在根目录创建 `pyproject.toml`，内容如下：

```toml
[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "metax"          # 你的包名
version = "0.1.0"
description = "A minimal example package"
authors = [
    {name = "Your Name", email = "you@example.com"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
```

如果不想写 `README.md`，可以暂时省略 `readme` 字段。

---

### 🛠️ 4. 安装打包工具

确保你已安装最新版的 `build` 和 `twine`：

```bash
pip install --upgrade build twine
```

---

### 🔨 5. 构建发布包

在根目录（包含 `pyproject.toml` 的那个目录）下执行：

```bash
python -m build
```

运行后会在 `dist/` 文件夹中生成两个文件：
*   `metax-0.1.0.tar.gz`（源码包）
*   `metax-0.1.0-py3-none-any.whl`（wheel包）

---

### 📤 6. 上传到 PyPI

**先用 TestPyPI 测试（推荐）**  
TestPyPI 是沙盒环境，不会影响正式索引。

```bash
twine upload -r testpypi dist/*
```

会让你输入 TestPyPI 账号（需要提前在 https://test.pypi.org 注册）。测试成功后，可尝试安装验证：

```bash
pip install -i https://test.pypi.org/simple/ metax
```

**上传到正式 PyPI**  
确认无误后，执行：

```bash
twine upload dist/*
```

会让你输入 PyPI 官网账号（https://pypi.org 注册）。

---

### 🧪 7. 安装与验证

上传成功后，任何人均可使用 `pip` 安装你的库：

```bash
pip install metax
```

然后在 Python 中测试：

```python
import metax
print(metax.hello("PyPI"))
```

---

### 📝 附：注册 PyPI 账号与 API Token

1. 前往 https://pypi.org 注册账号（也别忘了注册 TestPyPI 账号）。
2. 在账号设置中创建一个 API Token（建议用 token 替代密码，更安全）。
3. 上传时用 `__token__` 作为用户名，token 值作为密码。

---

### 🔁 更新版本

之后每次更新库，只需修改 `pyproject.toml` 中的 `version`，重新执行 `python -m build` 和 `twine upload dist/*` 即可（旧版本文件不会被覆盖，PyPI 会保留所有历史版本）。

这就是最简的发布流程。如果你有任何步骤遇到问题，或者想添加依赖包、命令行入口等，随时可以继续问我。