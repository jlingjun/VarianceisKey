# VarianceisKey

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## English

### Overview

**VarianceisKey** is a local-first AI text detection MCP (Model Context Protocol) server based on text variance analysis. It detects AI-generated text by analyzing how Large Language Models perceive changes in perplexity when text is modified.

**Key Features:**
- 🔒 **Local-first**: No cloud dependencies, all processing happens locally
- 🌐 **Multi-language Support**: Theoretically applicable to multiple languages (currently optimized for English, more languages coming soon)
- 💻 **Low Hardware Requirements**: Uses Qwen3-0.6B model, runnable on consumer GPUs
- 🔧 **Easy Integration**: Works with Claude Desktop, Trae IDE, Cursor, and other MCP clients
- 🐳 **Docker Ready**: Simple deployment with pre-built Docker images

### How It Works

The detection algorithm is based on the **VarianceisKey** principle:

1. **Text Variation**: The input text is rewritten multiple times using an LLM
2. **Perplexity Analysis**: The detection model calculates perplexity for the original and rewritten versions
3. **Variance Calculation**: The algorithm computes the variance of perplexity scores
4. **Classification**: Based on the variance pattern, the text is classified as "likely_ai" or "likely_human"

**Why Qwen3-0.6B?**

We chose the 0.6B parameter model to ensure that individual users can easily run this detector on consumer GPUs. If you have access to more powerful hardware, you can easily swap in larger models. We will maintain threshold values for different models in future updates.

### Quick Start

#### Prerequisites

- Docker and Docker Compose
- Node.js 18+
- An OpenAI-compatible API for text variation (or use your own LLM endpoint)

#### Method 1: Using Pre-built Images (Recommended)

```bash
# 1. Pull the Docker image
docker pull merumeru/varianceiskey:latest

# 2. Install the MCP server globally
npm install -g mcp-varianceiskey

# 3. Create configuration file
mkdir -p ~/varianceiskey
cat > ~/varianceiskey/.env << EOF
DETECT_MODEL_PATH=Qwen/Qwen3-0.6B
DETECT_DEVICE=cuda:0
DETECT_MAX_LENGTH=512
DETECT_MIN_TOKENS=128
GEN_LLM_BASE_URL=https://api.openai.com/v1
GEN_LLM_API_KEY=your-api-key
GEN_LLM_MODEL=gpt-3.5-turbo
EMPIRICAL_THRESHOLD=2.6351518630981445
EOF

# 4. Start the detector service
docker run -d \
  --name varianceiskey \
  -p 8765:8000 \
  --gpus all \
  -v ~/varianceiskey/.env:/app/.env \
  merumeru/varianceiskey:latest

# 5. Configure your MCP client
```

#### Method 2: Build from Source

```bash
# 1. Clone the repository
git clone https://github.com/jlingjun/VarianceisKey.git
cd VarianceisKey

# 2. Configure environment
cd deploy/local
cp .env.example .env
# Edit .env with your settings

# 3. Start services
docker-compose up -d

# 4. Build MCP server
cd ../../apps/mcp-local-ts
npm install
npm run build
```

### MCP Client Configuration

Add the following to your MCP client configuration:

**Claude Desktop** (`%APPDATA%\Claude\claude_desktop_config.json` on Windows):

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "mcp-varianceiskey",
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

**Trae IDE** (`%APPDATA%\Trae CN\User\mcp.json`):

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "mcp-varianceiskey",
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

**Using local build:**

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "node",
      "args": ["/path/to/VarianceisKey/apps/mcp-local-ts/dist/cli.js"],
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

### Configuration Reference

| Variable | Default | Description |
|----------|---------|-------------|
| `DETECT_MODEL_PATH` | `Qwen/Qwen3-0.6B` | HuggingFace model path or local path |
| `DETECT_DEVICE` | `cuda:0` | Device for inference (`cpu`, `cuda:0`, `cuda:1`) |
| `DETECT_MAX_LENGTH` | `512` | Maximum token length |
| `DETECT_MIN_TOKENS` | `128` | Minimum tokens required for detection |
| `GEN_LLM_BASE_URL` | - | OpenAI-compatible API endpoint for text variation |
| `GEN_LLM_API_KEY` | - | API key for the variation LLM |
| `GEN_LLM_MODEL` | - | Model name for variation |
| `EMPIRICAL_THRESHOLD` | `2.6351518630981445` | Threshold for classification (model-specific) |
| `DETECTOR_PORT` | `8765` | Port for the detector API |

### Tool: detect_text

**Input:**
```json
{
  "text": "Your text to analyze"
}
```

**Output:**
```json
{
  "label": "likely_ai",
  "score": 0.1948,
  "model_name": "Qwen3-0.6B"
}
```

- `label`: `likely_ai` or `likely_human`
- `score`: Varybalance score (lower = more likely AI-generated)
- `model_name`: The model used for detection

### Using Different Models

You can use any causal language model from HuggingFace:

```bash
# Example: Using a larger model
DETECT_MODEL_PATH=Qwen/Qwen2.5-1.5B

# Example: Using a local model
DETECT_MODEL_PATH=/models/my-custom-model
```

**Note:** Different models require different `EMPIRICAL_THRESHOLD` values. We will provide a calibration guide in future updates.

### Project Structure

```
VarianceisKey/
├── apps/
│   ├── detector-py/          # Python FastAPI detection service
│   │   ├── app/
│   │   │   ├── core/         # Detection algorithm
│   │   │   ├── model/        # Model loader
│   │   │   ├── utils/        # Text variation utilities
│   │   │   └── api/          # REST API routes
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── mcp-local-ts/         # TypeScript MCP server
│       ├── src/
│       ├── dist/
│       ├── package.json
│       └── tsconfig.json
├── deploy/
│   └── local/                # Local deployment configs
│       ├── docker-compose.yml
│       └── .env.example
├── docs/                     # Documentation
└── .github/
    └── workflows/            # CI/CD pipelines
```

### Documentation

- [Quick Start Guide](docs/quickstart.md)
- [Architecture Overview](docs/architecture.md)
- [MCP Configuration](docs/mcp-config.md)
- [Publishing Guide](docs/publish-guide.md)

### Roadmap

- [ ] Support for more languages (Chinese, Japanese, etc.)
- [ ] Calibration guide for different models
- [ ] Pre-calibrated thresholds for popular models
- [ ] Web UI for easy testing
- [ ] Batch detection API

### License

MIT License - See [LICENSE](LICENSE) for details.

---

<a name="中文"></a>

## 中文

### 概述

**VarianceisKey** 是一个基于文本变化分析的本地优先 AI 文本检测 MCP（Model Context Protocol）服务器。它通过分析大语言模型对文本修改后困惑度变化的感知来检测 AI 生成的文本。

**主要特性：**
- 🔒 **本地优先**：无云端依赖，所有处理在本地完成
- 🌐 **多语言支持**：理论上适用于多种语言（目前针对英文优化，后续将支持更多语言）
- 💻 **低硬件要求**：使用 Qwen3-0.6B 模型，可在消费级 GPU 上运行
- 🔧 **易于集成**：支持 Claude Desktop、Trae IDE、Cursor 等 MCP 客户端
- 🐳 **Docker 就绪**：提供预构建的 Docker 镜像，部署简单

### 工作原理

检测算法基于 **VarianceisKey** 原理：

1. **文本变体生成**：使用 LLM 对输入文本进行多次重写
2. **困惑度分析**：检测模型计算原文和重写版本的困惑度
3. **方差计算**：算法计算困惑度分数的方差
4. **分类判断**：根据方差模式，将文本分类为 "likely_ai" 或 "likely_human"

**为什么选择 Qwen3-0.6B？**

我们选择 0.6B 参数量的模型是为了确保个人用户可以在消费级 GPU 上轻松运行此检测器。如果您有更强大的算力，可以轻松替换为更大的模型。我们将在后续更新中维护不同模型的阈值参数。

### 快速开始

#### 前置条件

- Docker 和 Docker Compose
- Node.js 18+
- 一个 OpenAI 兼容的 API 用于文本变体生成（或使用您自己的 LLM 端点）

#### 方式一：使用预构建镜像（推荐）

```bash
# 1. 拉取 Docker 镜像
docker pull merumeru/varianceiskey:latest

# 2. 全局安装 MCP 服务器
npm install -g mcp-varianceiskey

# 3. 创建配置文件
mkdir -p ~/varianceiskey
cat > ~/varianceiskey/.env << EOF
DETECT_MODEL_PATH=Qwen/Qwen3-0.6B
DETECT_DEVICE=cuda:0
DETECT_MAX_LENGTH=512
DETECT_MIN_TOKENS=128
GEN_LLM_BASE_URL=https://api.openai.com/v1
GEN_LLM_API_KEY=your-api-key
GEN_LLM_MODEL=gpt-3.5-turbo
EMPIRICAL_THRESHOLD=2.6351518630981445
EOF

# 4. 启动检测服务
docker run -d \
  --name varianceiskey \
  -p 8765:8000 \
  --gpus all \
  -v ~/varianceiskey/.env:/app/.env \
  merumeru/varianceiskey:latest

# 5. 配置 MCP 客户端
```

#### 方式二：从源码构建

```bash
# 1. 克隆仓库
git clone https://github.com/jlingjun/VarianceisKey.git
cd VarianceisKey

# 2. 配置环境变量
cd deploy/local
cp .env.example .env
# 编辑 .env 文件

# 3. 启动服务
docker-compose up -d

# 4. 构建 MCP 服务器
cd ../../apps/mcp-local-ts
npm install
npm run build
```

### MCP 客户端配置

将以下内容添加到您的 MCP 客户端配置中：

**Claude Desktop**（Windows: `%APPDATA%\Claude\claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "mcp-varianceiskey",
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

**Trae IDE**（`%APPDATA%\Trae CN\User\mcp.json`）：

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "mcp-varianceiskey",
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

**使用本地构建：**

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "node",
      "args": ["/path/to/VarianceisKey/apps/mcp-local-ts/dist/cli.js"],
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

### 配置参数说明

| 变量 | 默认值 | 描述 |
|------|--------|------|
| `DETECT_MODEL_PATH` | `Qwen/Qwen3-0.6B` | HuggingFace 模型路径或本地路径 |
| `DETECT_DEVICE` | `cuda:0` | 推理设备（`cpu`、`cuda:0`、`cuda:1`） |
| `DETECT_MAX_LENGTH` | `512` | 最大 token 长度 |
| `DETECT_MIN_TOKENS` | `128` | 检测所需的最小 token 数 |
| `GEN_LLM_BASE_URL` | - | 用于文本变体的 OpenAI 兼容 API 端点 |
| `GEN_LLM_API_KEY` | - | 变体 LLM 的 API 密钥 |
| `GEN_LLM_MODEL` | - | 变体生成使用的模型名称 |
| `EMPIRICAL_THRESHOLD` | `2.6351518630981445` | 分类阈值（因模型而异） |
| `DETECTOR_PORT` | `8765` | 检测器 API 端口 |

### 工具：detect_text

**输入：**
```json
{
  "text": "要分析的文本"
}
```

**输出：**
```json
{
  "label": "likely_ai",
  "score": 0.1948,
  "model_name": "Qwen3-0.6B"
}
```

- `label`：`likely_ai`（可能是 AI 生成）或 `likely_human`（可能是人类撰写）
- `score`：Varybalance 分数（越低越可能是 AI 生成）
- `model_name`：用于检测的模型名称

### 使用其他模型

您可以使用 HuggingFace 上的任何因果语言模型：

```bash
# 示例：使用更大的模型
DETECT_MODEL_PATH=Qwen/Qwen2.5-1.5B

# 示例：使用本地模型
DETECT_MODEL_PATH=/models/my-custom-model
```

**注意：** 不同模型需要不同的 `EMPIRICAL_THRESHOLD` 值。我们将在后续更新中提供校准指南。

### 项目结构

```
VarianceisKey/
├── apps/
│   ├── detector-py/          # Python FastAPI 检测服务
│   │   ├── app/
│   │   │   ├── core/         # 检测算法
│   │   │   ├── model/        # 模型加载器
│   │   │   ├── utils/        # 文本变体工具
│   │   │   └── api/          # REST API 路由
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── mcp-local-ts/         # TypeScript MCP 服务器
│       ├── src/
│       ├── dist/
│       ├── package.json
│       └── tsconfig.json
├── deploy/
│   └── local/                # 本地部署配置
│       ├── docker-compose.yml
│       └── .env.example
├── docs/                     # 文档
└── .github/
    └── workflows/            # CI/CD 流水线
```

### 文档

- [快速开始指南](docs/quickstart.md)
- [架构概览](docs/architecture.md)
- [MCP 配置](docs/mcp-config.md)
- [发布指南](docs/publish-guide.md)

### 路线图

- [ ] 支持更多语言（中文、日文等）
- [ ] 不同模型的校准指南
- [ ] 热门模型的预校准阈值
- [ ] 易于测试的 Web UI
- [ ] 批量检测 API

### 许可证

MIT License - 详见 [LICENSE](LICENSE)。
