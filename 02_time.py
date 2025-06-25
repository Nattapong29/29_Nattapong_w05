from datetime import datetime, date, timedelta
import time 

today = date.today()

#print(f"วันที่ {today}")
#print(f"เดือน {today.month}")
#print(f"ปี {today.year}")

now = datetime.now()
#print(f"เวลาปัจจุบัน Hr : {now.hour}")
#print(f"เวลาปัจจุบัน m : {now.minute}")
#print(f"เวลาปัจจุบัน s : {now.second}")

# จัด Format ว ด ป 
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H-%M")




#คำนวนวนที่ 
tomorow = today + timedelta(days=1)
yesterday = today - timedelta(days= 1)
today = today + timedelta(days=1)
next_week  = today + timedelta(days=13)
next_monut = today + timedelta(days=30)
print(next_week)

