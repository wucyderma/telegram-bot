from telegram import Bot
import csv
import random
import schedule
import time
import threading
import os

# 取得環境變數
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# 日文單字資料
def load_vocab():
    return [
        {"日文": "猫", "假名": "ねこ", "中文": "貓", "例句": "私は猫が好きです。"},
        {"日文": "犬", "假名": "いぬ", "中文": "狗", "例句": "この犬はとてもかわいいです。"},
        {"日文": "学校", "假名": "がっこう", "中文": "學校", "例句": "明日、学校へ行きます。"},
        {"日文": "先生", "假名": "せんせい", "中文": "老師", "例句": "私の先生はとても優しいです。"},
        {"日文": "友達", "假名": "ともだち", "中文": "朋友", "例句": "友達と映画を見ました。"},
        {"日文": "本", "假名": "ほん", "中文": "書", "例句": "この本は面白いです。"},
        {"日文": "車", "假名": "くるま", "中文": "車", "例句": "新しい車を買いました。"},
        {"日文": "水", "假名": "みず", "中文": "水", "例句": "水をたくさん飲みます。"},
        {"日文": "映画", "假名": "えいが", "中文": "電影", "例句": "昨日、映画を見ました。"},
        {"日文": "食べ物", "假名": "たべもの", "中文": "食物", "例句": "日本の食べ物が好きです。"},
    ]

# 隨機選擇 10 個單字
def get_daily_vocab():
    vocab_list = load_vocab()
    return random.sample(vocab_list, 10)

# 發送 Telegram 訊息
def send_telegram_message():
    vocab_list = get_daily_vocab()
    message_text = "📖 今日の単語：\n" + "\n".join(
        [f"{v['日文']} ({v['假名']}) - {v['中文']}\n例: {v['例句']}" for v in vocab_list]
    )

    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message_text)

# 設定排程，每天早上 8 點發送
schedule.every().day.at("08:00").do(send_telegram_message)

# 讓排程在背景執行
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_scheduler).start()
