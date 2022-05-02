import BOTZERA
import time
import schedule


schedule.every(10).seconds.do(BOTZERA.boss_hunt)

while True:
    schedule.run_pending()
    time.sleep(0.5)
