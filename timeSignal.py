# @jihou_kita version 2.0 timeSignal.py

# 標準ライブラリ
import time

# 外部ライブラリ
import schedule

# Misskey.py
from misskey import Misskey
mk = Misskey("misskirara.net", i="***")

# 関数
def timeSignal02():
    mk.notes_create(text="> 「生活リズム 規則的に」" + "\n" + "> 「夜更かしお寝坊 だめゼッタイ」")
def timeSignal08():
    mk.notes_create(text=":ohayougozaimasu_:")
def timeSignal18():
    mk.notes_create(text=":mousugu_tokeiha6ji:")
def timeSignal20():
    mk.notes_create(text=":mousugu_tokeiha8ji:")

# 指定時刻
schedule.every().day.at("01:55").do(timeSignal02)
schedule.every().day.at("07:55").do(timeSignal08)
schedule.every().day.at("17:55").do(timeSignal18)
schedule.every().day.at("19:55").do(timeSignal20)

# 指定時刻に関数を実行
while True:
    schedule.run_pending()
    time.sleep(1)
