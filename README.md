# Humanity Protocol 腳本 docker compose v2版本
基於 https://github.com/GzGod/Humanitybot 修改

## Docker部署方法

使用Docker可以更方便地部署腳本，並確保重啟容器後不會重複執行操作。

### 1. 準備配置文件

確保已經創建並填寫好以下文件：
- `private_keys.txt`：包含私鑰列表
- `proxy.txt`（可選）：包含代理列表

### 2. 使用Docker Compose部署

首先確保您已安裝Docker和Docker Compose，然後執行：

```bash
# 構建並在後台啟動容器
docker compose up -d
```

### 3. 查看運行日誌

```bash
# 查看容器日誌
docker logs -f humanity-bot
```

### 4. 停止和重啟

```bash
# 停止容器
docker compose down

# 重新啟動
docker compose up -d
```

### 5. 數據持久化

所有狀態數據都保存在名為`humanity_bot_data`的Docker卷中，確保重啟容器或服務器後不會重複執行操作。

##部署說明

在Ubuntu部署：

1. 安裝Docker和Docker Compose

```bash
# 更新系統
sudo apt update && sudo apt upgrade -y

# 安裝所需依賴
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# 添加Docker官方GPG密鑰
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 設置Docker穩定版存儲庫
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 更新apt包索引
sudo apt update

# 安裝Docker Engine
sudo apt install -y docker-ce docker-ce-cli containerd.io

# 將當前用戶添加到docker組（可選，避免使用sudo運行docker命令）
sudo usermod -aG docker $USER

# 安裝Docker Compose V2
sudo apt install -y docker-compose-plugin
```

設置

```bash

# 創建並編輯private_keys.txt
nano private_keys.txt
# 添加您的私鑰，每行一個

# 如需使用代理，創建並編輯proxy.txt（可選）
nano proxy.txt
# 添加您的代理，每行一個
```

部署和管理

```bash
# 啟動
docker compose up -d

# 查看日誌
docker logs -f humanity-bot

# 停止
docker compose down
```
