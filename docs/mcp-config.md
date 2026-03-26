# MCP Configuration / MCP 配置

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## English

### Claude Desktop

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

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

### Trae IDE

**Windows**: `%APPDATA%\Trae CN\User\mcp.json`

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

### Cursor

Add to your MCP configuration:

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

### Using Local Build

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

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DETECTOR_API_URL` | `http://127.0.0.1:8765` | Detector API endpoint |

---

<a name="中文"></a>

## 中文

### Claude Desktop

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

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

### Trae IDE

**Windows**: `%APPDATA%\Trae CN\User\mcp.json`

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

### Cursor

添加到您的 MCP 配置中：

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

### 使用本地构建

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

### 环境变量

| 变量 | 默认值 | 描述 |
|------|--------|------|
| `DETECTOR_API_URL` | `http://127.0.0.1:8765` | 检测器 API 端点 |
