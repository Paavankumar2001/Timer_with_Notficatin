



import time as t
import datetime as dt
import winsound as ws
#import playsound as ps
#ps.playsound(r"C:\\Users\\paava\\Desktop\\New folder\\sd.mp3")

def counter(T, remindBuffer):
    remindBuffer = remindBuffer * 60
    actTime = T

    while T > 0:
        if T % remindBuffer == 0 or round(T/actTime*100) == 17:
            ws.Beep(5550,2)
        
        timer = dt.timedelta(seconds = T)
        print(timer, end="\r")
        t.sleep(1)
        T -= 1
    print("Bzzz! Countdown at zero!!!")
    ws.Beep(5550,300)


#takes input in hours the timer is to be set
def hoursTimer():
    H = int(input("Set Timer in hours: "))
    rem = int(input("Remind every __ in minutes: "))
    if H > 3:
        print("Set an alarm")
    else:
        H = H*3600
        counter(H,rem)

#takes input in minutes the timer is to be set
def minutesTimer():
    M = int(input("Set Timer in Minutes: "))
    rem = int(input("Remind every __ in minutes: "))
    if M > 180:
        print("Set an alarm")
    else:
        M = M*60
        counter(M,rem)

#takes input in seconds the timer is to be set
def secondsTimer():
    S = int(input("Set Timer in Seconds: "))
    rem = int(input("Remind every __ in minutes: "))
    if S > 10000:
        print("Set an alarm")
    else:
        counter(S,rem)

#takes input in datetime format the timer is to be set
def standardTimer():
    H = int(input("Number in hours: "))
    M = int(input("Number in minutes: "))
    S = int(input("Number in seconds: "))
    rem = int(input("Remind every __ in minutes: "))
    if H > 3:
        print("Set an alarm")
    else:
        T = H*3600 + M * 60 + S
        counter(T,rem)



while True:
    print("Select time in \n1. Hours\n2. Minutes\n3. Seconds\n4. Classic")
    N = int(input())
    if N == 1:
        print(hoursTimer())
        break
    elif N == 2:
        minutesTimer()
        break
    elif N == 3:
        secondsTimer()
        break
    elif N == 4:
        standardTimer()
        break
    else:
        print("Choose suitable type")
        continue