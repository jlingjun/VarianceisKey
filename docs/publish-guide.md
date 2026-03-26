# Publishing Guide / 发布指南

[English](#english) | [中文](#中文)

---

<a name="english"></a>

## English

### Prerequisites

1. Docker Hub account
2. npm account
3. GitHub repository with Secrets configured

### Docker Image

**Manual:**
```bash
docker login
cd apps/detector-py
docker build -t yourname/varianceiskey:latest .
docker push yourname/varianceiskey:latest
```

**GitHub Actions (Recommended):**

1. Set GitHub Secrets:
   - `DOCKERHUB_USERNAME`: Your Docker Hub username
   - `DOCKERHUB_TOKEN`: Docker Hub Access Token

2. Push a tag:
```bash
git tag v1.0.0
git push --tags
```

### npm Package

```bash
cd apps/mcp-local-ts
npm run build
npm login
npm publish
```

### Version Update

```bash
# Update Docker image
docker pull yourname/varianceiskey:latest

# Update npm package
npm update -g mcp-varianceiskey
```

---

<a name="中文"></a>

## 中文

### 前置条件

1. Docker Hub 账号
2. npm 账号
3. 配置了 Secrets 的 GitHub 仓库

### Docker 镜像

**手动发布：**
```bash
docker login
cd apps/detector-py
docker build -t yourname/varianceiskey:latest .
docker push yourname/varianceiskey:latest
```

**GitHub Actions（推荐）：**

1. 设置 GitHub Secrets：
   - `DOCKERHUB_USERNAME`: Docker Hub 用户名
   - `DOCKERHUB_TOKEN`: Docker Hub Access Token

2. 推送 tag：
```bash
git tag v1.0.0
git push --tags
```

### npm 包

```bash
cd apps/mcp-local-ts
npm run build
npm login
npm publish
```

### 版本更新

```bash
# 更新 Docker 镜像
docker pull yourname/varianceiskey:latest

# 更新 npm 包
npm update -g mcp-varianceiskey
```
