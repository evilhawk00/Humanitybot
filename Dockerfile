FROM python:3.10-slim

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 只複製應用程式相關檔案
COPY main.py .
COPY README.md ./

# 設置時區為UTC
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 創建存儲上次執行時間文件的目錄和私鑰代理文件的目錄
RUN mkdir -p /data
RUN touch /app/private_keys.txt /app/proxy.txt

# 創建非root用戶
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 設置目錄權限
RUN chown -R appuser:appuser /app
RUN chown -R appuser:appuser /data
RUN chmod 644 /app/private_keys.txt /app/proxy.txt

# 設置卷，保存上次執行時間的數據
VOLUME ["/data"]

# 設置環境變數指向數據目錄
ENV LAST_RUN_FILE=/data/last_run_timestamp.json

# 切換到非root用戶
USER appuser

# 運行腳本
CMD ["python", "main.py"] 