# Local Deployment

## Quick Start

1. Copy environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your settings

3. Start the service:
```bash
docker-compose up -d
```

## Configuration

| Variable | Description |
|----------|-------------|
| DETECT_MODEL_PATH | Path to model files in container |
| DETECT_DEVICE | cpu or cuda |
| DETECT_MAX_LENGTH | Max tokenization length |
| GEN_LLM_BASE_URL | LLM endpoint (future use) |
| GEN_LLM_API_KEY | LLM API key (future use) |
| GEN_LLM_MODEL | LLM model name (future use) |

## Model Setup

Place your model files in `./models/` directory:

```
models/
└── your-detector-model/
    ├── config.json
    ├── pytorch_model.bin
    └── tokenizer files...
```

Update `DETECT_MODEL_PATH` in `.env` to match.

## API Endpoints

- `GET /health` - Health check
- `POST /detect` - Text detection

## Logs

```bash
docker-compose logs -f
```

## Stop

```bash
docker-compose down
```
