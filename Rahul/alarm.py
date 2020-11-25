import time, datetime
from time import sleep

date = datetime.date.isoformat(datetime.date.today())
print(date)
hour = input("Tell the alarm hour in 24 format ** Only for TODAY ** :- ")
mint = input("Tell the alarm minitues ** Only for TODAY **:-  ")
flag = 1
while flag == 1:
    hour1 = time.strftime("%H")
    mint1 = time.strftime("%M")

    if hour1 == hour:
        pass
        if mint1 == mint:
            print(" NOTIFICATION FOR ALARM \n WEAK UP , WEAK UP ")
            sleep(5)
            flag = 0
        else:
            print(hour1, mint1)
            sleep(5)
    else:
        pass


print(" ALARM turn off ")
