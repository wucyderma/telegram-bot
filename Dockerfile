# 使用 Python 3.9 作為基礎環境
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製程式碼到容器內
COPY . /app

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 指定 Cloud Run 啟動指令
CMD ["python", "bot.py"]
