"""文件操作工具"""

import os
import shutil
import json
import hashlib
from pathlib import Path
from typing import Optional, List, Union, Dict, Any


def read_text(file_path: str, encoding: str = "utf-8") -> str:
    """读取文本文件

    Args:
        file_path: 文件路径
        encoding: 编码格式，默认为utf-8

    Returns:
        文件内容

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()


def write_text(file_path: str, content: str, encoding: str = "utf-8") -> None:
    """写入文本文件

    Args:
        file_path: 文件路径
        content: 文件内容
        encoding: 编码格式，默认为utf-8
    """
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(content)


def read_lines(file_path: str, encoding: str = "utf-8") -> List[str]:
    """按行读取文件

    Args:
        file_path: 文件路径
        encoding: 编码格式，默认为utf-8

    Returns:
        行列表

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.readlines()


def write_lines(file_path: str, lines: List[str], encoding: str = "utf-8") -> None:
    """写入多行到文件

    Args:
        file_path: 文件路径
        lines: 行列表
        encoding: 编码格式，默认为utf-8
    """
    with open(file_path, 'w', encoding=encoding) as f:
        f.writelines(lines)


def read_json(file_path: str, encoding: str = "utf-8") -> Dict[str, Any]:
    """读取JSON文件

    Args:
        file_path: 文件路径
        encoding: 编码格式，默认为utf-8

    Returns:
        JSON数据

    Raises:
        FileNotFoundError: 文件不存在时抛出
        json.JSONDecodeError: JSON解析失败时抛出
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)


def write_json(file_path: str, data: Dict[str, Any], encoding: str = "utf-8", indent: int = 2) -> None:
    """写入JSON文件

    Args:
        file_path: 文件路径
        data: JSON数据
        encoding: 编码格式，默认为utf-8
        indent: 缩进空格数，默认为2
    """
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def exists(file_path: str) -> bool:
    """判断文件或目录是否存在

    Args:
        file_path: 文件或目录路径

    Returns:
        是否存在
    """
    return os.path.exists(file_path)


def is_file(file_path: str) -> bool:
    """判断是否为文件

    Args:
        file_path: 路径

    Returns:
        是否为文件
    """
    return os.path.isfile(file_path)


def is_dir(file_path: str) -> bool:
    """判断是否为目录

    Args:
        file_path: 路径

    Returns:
        是否为目录
    """
    return os.path.isdir(file_path)


def get_size(file_path: str) -> int:
    """获取文件大小（字节）

    Args:
        file_path: 文件路径

    Returns:
        文件大小

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    return os.path.getsize(file_path)


def get_extension(file_path: str) -> str:
    """获取文件扩展名

    Args:
        file_path: 文件路径

    Returns:
        扩展名（包含点号，如".txt"）
    """
    return os.path.splitext(file_path)[1]


def get_filename(file_path: str) -> str:
    """获取文件名（包含扩展名）

    Args:
        file_path: 文件路径

    Returns:
        文件名
    """
    return os.path.basename(file_path)


def get_basename(file_path: str) -> str:
    """获取文件名（不包含扩展名）

    Args:
        file_path: 文件路径

    Returns:
        文件名（不包含扩展名）
    """
    return os.path.splitext(os.path.basename(file_path))[0]


def get_parent(file_path: str) -> str:
    """获取父目录路径

    Args:
        file_path: 文件路径

    Returns:
        父目录路径
    """
    return os.path.dirname(file_path)


def join_path(*paths: str) -> str:
    """拼接路径

    Args:
        *paths: 路径片段

    Returns:
        拼接后的路径
    """
    return os.path.join(*paths)


def create_dir(dir_path: str) -> None:
    """创建目录（支持多级）

    Args:
        dir_path: 目录路径
    """
    os.makedirs(dir_path, exist_ok=True)


def delete_file(file_path: str) -> None:
    """删除文件

    Args:
        file_path: 文件路径

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    os.remove(file_path)


def delete_dir(dir_path: str, force: bool = False) -> None:
    """删除目录

    Args:
        dir_path: 目录路径
        force: 是否强制删除（包含内容），默认为False

    Raises:
        OSError: 目录非空且force为False时抛出
    """
    if force:
        shutil.rmtree(dir_path)
    else:
        os.rmdir(dir_path)


def copy_file(src: str, dst: str) -> None:
    """复制文件

    Args:
        src: 源文件路径
        dst: 目标文件路径
    """
    shutil.copy2(src, dst)


def copy_dir(src: str, dst: str) -> None:
    """复制目录

    Args:
        src: 源目录路径
        dst: 目标目录路径
    """
    shutil.copytree(src, dst)


def move(src: str, dst: str) -> None:
    """移动文件或目录

    Args:
        src: 源路径
        dst: 目标路径
    """
    shutil.move(src, dst)


def rename(src: str, dst: str) -> None:
    """重命名文件或目录

    Args:
        src: 原路径
        dst: 新路径
    """
    os.rename(src, dst)


def list_files(dir_path: str, pattern: str = "*") -> List[str]:
    """列出目录下的文件

    Args:
        dir_path: 目录路径
        pattern: 文件模式，默认为"*"

    Returns:
        文件路径列表
    """
    path = Path(dir_path)
    return [str(f) for f in path.glob(pattern) if f.is_file()]


def list_dirs(dir_path: str) -> List[str]:
    """列出目录下的子目录

    Args:
        dir_path: 目录路径

    Returns:
        子目录路径列表
    """
    path = Path(dir_path)
    return [str(d) for d in path.iterdir() if d.is_dir()]


def get_md5(file_path: str) -> str:
    """计算文件MD5值

    Args:
        file_path: 文件路径

    Returns:
        MD5值（32位小写）

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_sha256(file_path: str) -> str:
    """计算文件SHA256值

    Args:
        file_path: 文件路径

    Returns:
        SHA256值（64位小写）

    Raises:
        FileNotFoundError: 文件不存在时抛出
    """
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()
