# Humanity Protocol 脚本

[点击注册➡](https://testnet.humanity.org/login?ref=xuegaozs)

## 介绍
脚本每天自动 Humanity Protocol 签到领取 $RWT 奖励。

## 使用方法

按照以下步骤设置并运行脚本。

### 1. 克隆存储库

首先，使用 Git 将此存储库克隆到本地计算机：

```bash
git clone https://github.com/Gzgod/Humanitybot.git
```

### 2. 将目录更改为克隆文件夹

导航到克隆存储库的文件夹：

```bash
cd Humanitybot
```

### 3. 填写private_keys.txt
将私钥填入private_keys.txt文件。该文件每行应包含一个私钥，如下所示：

```python
private_key_1
private_key_2
private_key_3
...
```
### 2025.1.1更新，增加了代理功能
格式 
```bash
http://user:password@ip:port
```

### 4. 安装依赖项

```bash
pip install -r requirements.txt
```

### 5. 运行脚本

```bash
python3 main.py
```
