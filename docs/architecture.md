# Architecture / 架构

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## English

### System Overview

```
MCP Client (Claude/Trae/Cursor)
        ↓ stdio
TypeScript MCP Server (mcp-varianceiskey)
        ↓ HTTP
Python Detector Service (varianceiskey:latest)
        ↓
HuggingFace Model (Qwen3-0.6B)
```

### Components

| Component | Technology | Description |
|-----------|------------|-------------|
| MCP Server | TypeScript + MCP SDK | Handles stdio communication with MCP clients |
| Detector Service | Python + FastAPI | Performs text detection inference |
| Detection Model | PyTorch + Transformers | Causal LM for perplexity analysis |
| Variation LLM | OpenAI API | Generates text variations for comparison |

### Data Flow

1. MCP client calls `detect_text` tool with input text
2. MCP Server forwards request to Detector Service via HTTP
3. Detector Service:
   - Generates text variations using Variation LLM
   - Calculates perplexity for each variation
   - Computes variance-based score
   - Classifies text as AI or human
4. Result returns through the chain

### Key Design Decisions

- **Local-first**: All inference happens locally, no data leaves your machine
- **Model flexibility**: Easy to swap detection models
- **Low hardware requirements**: Qwen3-0.6B runs on consumer GPUs

---

<a name="中文"></a>

## 中文

### 系统概览

```
MCP 客户端 (Claude/Trae/Cursor)
        ↓ stdio
TypeScript MCP 服务器 (mcp-varianceiskey)
        ↓ HTTP
Python 检测服务 (varianceiskey:latest)
        ↓
HuggingFace 模型 (Qwen3-0.6B)
```

### 组件说明

| 组件 | 技术 | 描述 |
|------|------|------|
| MCP 服务器 | TypeScript + MCP SDK | 处理与 MCP 客户端的 stdio 通信 |
| 检测服务 | Python + FastAPI | 执行文本检测推理 |
| 检测模型 | PyTorch + Transformers | 用于困惑度分析的因果语言模型 |
| 变体生成 LLM | OpenAI API | 生成用于比较的文本变体 |

### 数据流程

1. MCP 客户端调用 `detect_text` 工具，传入待检测文本
2. MCP 服务器通过 HTTP 将请求转发到检测服务
3. 检测服务：
   - 使用变体生成 LLM 生成文本变体
   - 讯算每个变体的困惑度
   - 计算基于方差的分数
   - 将文本分类为 AI 生成或人类撰写
4. 结果沿链路返回
### 关键设计决策

- **本地优先**： 所有推理在本地进行，数据不会离开您的机器
- **模型灵活性**： 可轻松替换检测模型
- **低硬件要求**： Qwen3-0.6B 可在消费级 GPU 上运行
