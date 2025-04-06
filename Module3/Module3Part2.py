#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem. Ask the user
# for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.
from operator import truediv

#Contants
HOURS_PER_DAY = 24


def calculateAlarm(current_time, alarm):
    print('Current Time', current_time)
    print('Alarm       ', alarm)

    return (current_time + alarm) % 24


def validateTime(time):
    if time >= 0 and time <= 23:
        return True
    else:
        return False


if __name__ == '__main__':
    current_time = int(input('Current Time(0-23):  \n'))
    alarm = int(input('Number of hours to wait for alarm: \n'))

    if validateTime(current_time):
        print('Alarm time: ', calculateAlarm(current_time,alarm))
    else:
        print('Invalid time entered. Please enter a time between 0 and 23.')
