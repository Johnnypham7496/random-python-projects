from datetime import datetime
import winsound


alarm_time = input("Enter the time of alarm to be set: HH:MM:SS\n")
# the square brackets represent the placement of the numbers within alarm_time
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11]

print("Setting up alarm..")

while True:
    now = datetime.now()
    # strftime is used to format a datetime aka 'string format time'
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    # multiple if statements to make sure the datetime matches with the alarm time that is entered 
    if alarm_period==current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_min:
                if alarm_second == current_sec:
                    print("WAKE UP")
                    winsound.Beep()
                    break