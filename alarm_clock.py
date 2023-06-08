from datetime import datetime
from winsound import PlaySound 


alarm_time = input("Enter the time of alarm to be set: HH:MM:SS\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11]

print("Setting up alarm..")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period==current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_min:
                if alarm_second == current_sec:
                    print("WAKE UP")
                    PlaySound()
                    break