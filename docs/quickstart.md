# Quick Start / 快速开始

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## English

Get VarianceisKey running in minutes with pre-built Docker images.

### Prerequisites

- Docker
- Node.js 18+
- NVIDIA GPU (recommended) or CPU

- OpenAI-compatible API key

### Step 1: Pull Docker Image

```bash
docker pull merumeru/varianceiskey:latest
```

### Step 2: Install MCP Server
```bash
npm install -g mcp-varianceiskey
```
### Step 3: Create Configuration
```bash
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
```
### Step 4: Start Service
```bash
docker run -d \
  --name varianceiskey \
  -p 8765:8000 \
  --gpus all \
  -v ~/varianceiskey/.env:/app/.env \
  merumeru/varianceiskey:latest
```
### Step 5: Configure MCP Client
Add to your MCP client config:

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

### Verify Installation
```bash
curl http://localhost:8765/health
# Expected: {"status": "ok"}
```

---

<a name="中文"></a>

## 中文

使用预构建的 Docker 镜像，几分钟内即可运行 VarianceisKey。

### 前置条件
- Docker
- Node.js 18+
- NVIDIA GPU（推荐）或 CPU
- OpenAI 兣容的 API 密钥

### 步骤 1：拉取 Docker 镜像
```bash
docker pull merumeru/varianceiskey:latest
```
### 步骤 2：安装 MCP 服务器
```bash
npm install -g mcp-varianceiskey
```
### 步骤 3：创建配置文件
```bash
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
```
### 步骤 4：启动服务
```bash
docker run -d \
  --name varianceiskey \
  -p 8765:8000 \
  --gpus all \
  -v ~/varianceiskey/.env:/app/.env \
  merumeru/varianceiskey:latest
```
### 步骤 5：配置 MCP 客户端
添加到您的 MCP 客户端配置中：

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

### 验证安装
```bash
curl http://localhost:8765/health
# 预期返回：{"status": "ok"}
```

