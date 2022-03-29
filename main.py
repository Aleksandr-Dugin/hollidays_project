from consts import *
import telegram
from parser_data import holidays
import datetime
from time import sleep
bot = telegram.Bot(token=TOKEN)


c = 366

day_count = 0

def day_count_in_year(): 
    time = datetime.datetime.now()
    time = time.strftime("%Y-%m-%d  %H:%M:%S")
    ans = int(time[8:10])
    
    return ans + (((int(time[6]) - 1) // 2) * 30) +  (((int(time[6]) - 1) // 2) * 31) 


day_count = day_count_in_year()




while True: 
 
    bot = telegram.Bot(token=TOKEN)

    updates = bot.get_updates()
    chat_id = bot.get_updates()[-1].message.chat_id
    if day_count == 59:
        continue
    



    bot.send_message(chat_id=chat_id, text=holidays[day_count])
    sleep(86400)
    day_count += 1

