# MCP VarianceisKey

TypeScript MCP Server for the VarianceisKey AI text detection system.

## Installation

```bash
npm install
npm run build
```

## Usage

### Global Installation (Recommended)

```bash
npm install -g mcp-varianceiskey
```

Then configure your MCP client:

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

### Local Development

```json
{
  "mcpServers": {
    "varianceiskey": {
      "command": "node",
      "args": ["/path/to/mcp-local-ts/dist/cli.js"],
      "env": {
        "DETECTOR_API_URL": "http://127.0.0.1:8765"
      }
    }
  }
}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DETECTOR_API_URL` | `http://127.0.0.1:8765` | Detector API endpoint |

## Tool: detect_text

**Input:**
```json
{
  "text": "Text to analyze"
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

## Documentation

See the [main documentation](../../README.md) for full setup instructions.
