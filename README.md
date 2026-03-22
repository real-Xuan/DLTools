<a id="readme-top"></a>

# DLTools

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Build](https://img.shields.io/badge/build-hatchling-FF6600)](https://hatch.pypa.io/latest/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

一个面向深度学习工作流的多领域工具箱，聚焦数据预处理与后处理，覆盖 CV、Radar/GPR、Signal、NLP、Audio、TimeSeries 等常见任务场景。

## 目录

- [DLTools](#dltools)
  - [目录](#目录)
  - [关于项目](#关于项目)
  - [功能概览](#功能概览)
  - [项目结构](#项目结构)
  - [快速开始](#快速开始)
    - [环境要求](#环境要求)
    - [安装（推荐：uv）](#安装推荐uv)
    - [安装（兼容 pip）](#安装兼容-pip)
  - [使用示例](#使用示例)
    - [1) CV: 生成 PSF](#1-cv-生成-psf)
    - [2) Radar: 批量读取并保存](#2-radar-批量读取并保存)
    - [3) NLP: 文本预处理与分词](#3-nlp-文本预处理与分词)
  - [开发与质量保障](#开发与质量保障)
    - [本地测试](#本地测试)
    - [代码质量](#代码质量)
    - [已有测试覆盖](#已有测试覆盖)
  - [Docker](#docker)
  - [贡献指南](#贡献指南)
  - [许可证](#许可证)

## 关于项目

DLTools 采用 `src` 布局与现代 Python 打包方式（`pyproject.toml` + Hatchling），核心目标是将跨领域的常用预处理能力沉淀为一致、可复用、可测试的 API。

适用场景：

- 模型训练前的数据清洗、标准化、增强
- 推理后处理和格式转换
- 多模态/多来源数据的工程化处理

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 功能概览

- CV: 运动模糊核生成、PSF 生成、基础增强接口
- Radar/GPR: `.DZT` 单文件读取、目录批量对齐读取、数组持久化（`.mat`/`.npy`）
- Signal: 低通/高通/带通滤波、滑动平均
- NLP: 文本规范化、去标点、基础分词
- Audio: 零交叉率、频谱、MFCC（可选依赖）
- TimeSeries: `z-score`、`min-max`、`robust` 缩放及特征函数

## 项目结构

```text
.
├── pyproject.toml
├── dockerfile
├── src/
│   └── dltools/
│       ├── core/
│       ├── cv/
│       ├── radar/
│       ├── signal/
│       ├── nlp/
│       ├── audio/
│       ├── timeseries/
│       ├── utils/
│       └── legacy/
└── tests/
```

## 快速开始

### 环境要求

- Python >= 3.10
- 建议使用 [uv](https://docs.astral.sh/uv/) 管理虚拟环境与依赖

### 安装（推荐：uv）

```bash
# 1) 创建虚拟环境
uv venv

# 2) 安装基础能力
uv pip install -e .

# 3) 安装开发依赖
uv pip install -e ".[dev]"
```

按领域安装可选依赖：

```bash
uv pip install -e ".[cv]"
uv pip install -e ".[radar]"
uv pip install -e ".[nlp]"
uv pip install -e ".[audio]"
uv pip install -e ".[timeseries]"
```

一次性安装全部可选能力：

```bash
uv pip install -e ".[all]"
```

### 安装（兼容 pip）

```bash
pip install -e .
pip install -e ".[dev]"
```

## 使用示例

### 1) CV: 生成 PSF

```python
import numpy as np
from dltools.cv import generate_psf

psf, anchor = generate_psf(length=21, angle=15.0)
print(psf.shape, anchor, np.sum(psf))
```

### 2) Radar: 批量读取并保存

```python
from dltools.radar import read_dzt_files_aligned, save_array

data = read_dzt_files_aligned("/path/to/dzt_dir")
save_array(data, "aligned.mat", file_type="mat")
```

### 3) NLP: 文本预处理与分词

```python
from dltools.nlp import normalize_text, remove_punctuation, basic_tokenize

text = normalize_text("Hello, DLTools!")
tokens = basic_tokenize(remove_punctuation(text))
print(tokens)  # ['hello', 'dltools']
```

## 开发与质量保障

### 本地测试

```bash
uv pip install -e ".[dev]"
pytest
```

### 代码质量

```bash
ruff check .
```

### 已有测试覆盖

- CV blur 基础行为测试
- Signal 滑动平均输出稳定性测试
- NLP 文本预处理与分词测试
- Audio 零交叉率范围测试
- TimeSeries 标准化与归一化测试

## Docker

```bash
docker build -t dltools -f dockerfile .
docker run --rm dltools
```


如果你有功能建议，欢迎通过 Issue 提交。

## 贡献指南

欢迎贡献代码、文档、测试与示例。推荐流程：

1. Fork 本仓库并创建特性分支。
2. 保持变更最小且聚焦，补充对应测试。
3. 在本地通过 `pytest` 和 `ruff check .`。
4. 发起 Pull Request，清晰描述动机、改动点和验证方式。
## 许可证

本项目在 `pyproject.toml` 中声明为 MIT License。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

