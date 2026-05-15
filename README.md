# MetaX

[![PyPI version](https://badge.fury.io/py/metax.svg)](https://badge.fury.io/py/metax)
[![Python](https://img.shields.io/pypi/pyversions/metax.svg)](https://pypi.org/project/metax/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

English | [中文](README_CN.md)

---

**MetaX** is a feature-rich Python utility library that provides common tools for mathematical operations, string processing, datetime handling, and file operations, helping developers improve productivity.

### 📖 Project Positioning

MetaX aims to be a helpful assistant for Python developers, providing:

- **🔢 Math Operations** - Basic operations, advanced math functions, number theory tools
- **📝 String Processing** - Formatting, validation, conversion tools
- **⏰ Datetime** - Time retrieval, calculation, formatting tools
- **📁 File Operations** - File I/O, path operations, hash calculation

All functions are carefully designed with complete type annotations and docstrings, supporting IDE auto-completion, ready to use out of the box.

### 🚀 Installation

#### Install with pip

```bash
pip install metax
```

#### Upgrade to Latest Version

```bash
pip install metax --upgrade
```

#### Install from TestPyPI (Testing Version)

```bash
pip install --index-url https://test.pypi.org/simple/ metax
```

### 💡 Quick Start

#### Basic Example

```python
import metax

# Greeting function
print(metax.hello("World"))  # Output: 你好, World!
```

#### Math Operations

```python
import metax

# Basic operations
print(metax.add(10, 5))        # Addition: 15
print(metax.subtract(10, 5))   # Subtraction: 5
print(metax.multiply(10, 5))   # Multiplication: 50
print(metax.divide(10, 5))     # Division: 2.0

# Advanced operations
print(metax.power(2, 3))       # Power: 8.0
print(metax.sqrt(16))          # Square root: 4.0
print(metax.factorial(5))      # Factorial: 120
```

#### String Processing

```python
import metax

# Formatting
print(metax.reverse("hello"))           # Reverse: olleh
print(metax.mask("13812345678", 3, 4))  # Mask: 138****5678
print(metax.format_size(1024000))       # File size: 1000.00 KB

# Validation
print(metax.is_email("test@example.com"))   # Email validation: True
print(metax.is_phone_cn("13812345678"))     # Phone validation: True
print(metax.is_url("https://example.com"))  # URL validation: True
```

#### Datetime

```python
import metax

print(metax.now())           # Current time: 2026-05-15 10:30:45
print(metax.timestamp())     # Timestamp: 1705285845
print(metax.today())         # Today's date: 2026-05-15
```

#### File Operations

```python
import metax

# File I/O
metax.write_text("test.txt", "Hello, MetaX!")
content = metax.read_text("test.txt")

# Path operations
path = metax.join_path("D:", "test", "file.txt")
print(metax.get_extension("test.txt"))  # Extension: .txt
```

### 📚 Documentation

#### Documentation Portal

- **[📖 Documentation Center](Docs/README.md)** - Complete documentation navigation

#### Detailed Docs

- **[🚀 Deployment Guide](Docs/Deploy.md)** - How to publish PyPI packages
- **[📖 Usage Guide](Docs/Usage.md)** - Detailed usage and API documentation
- **[🔄 Update Process](Docs/Update.md)** - Version update and release process

#### Changelog

- **[📝 CHANGELOG.md](CHANGELOG.md)** - Version update history

### 🔗 Important Links

#### PyPI

- **[PyPI Project Page](https://pypi.org/project/metax/)** - Official release
- **[TestPyPI Project Page](https://test.pypi.org/project/metax/)** - Testing version

#### GitHub

- **[GitHub Repository](https://github.com/ACANX/MetaX)** - Source code repository
- **[Issue Tracker](https://github.com/ACANX/MetaX/issues)** - Submit bugs or feature requests

### 📦 Feature Overview

| Module | Features | Function Count |
|--------|----------|----------------|
| Math Operations | Basic operations, advanced math, number theory | 17 |
| String Processing | Formatting, validation | 26 |
| Datetime | Time retrieval, calculation, judgment | 17 |
| File Operations | I/O, path, hash | 22 |

**Total: 82+ utility functions**

### 🎯 Use Cases

- **Data Processing** - Mathematical calculations, string processing
- **Form Validation** - Email, phone, ID card validation
- **Log Processing** - Time formatting, file operations
- **Tool Development** - Quick CLI tool building
- **Automation Scripts** - File processing, data conversion

### 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

#### Contribution Process

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

For detailed process, please refer to [Update Process Documentation](Docs/Update.md)

### 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details

### 📊 Version Information

- **Current Version**: 0.1.2
- **Python Version**: >= 3.8

### 🌟 Star History

If this project helps you, please give it a ⭐️ Star!

---

**Made with ❤️ by ACANX**
